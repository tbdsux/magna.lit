import { Router } from "express";
import { body } from "express-validator";
import { libDB } from "../lib/base";
import { LibraryMangaProps } from "../typings/library";

const libraryRouter = Router();

// fetch items from library
libraryRouter.get("/", async (req, res) => {
  let { items, last } = await libDB.fetch({}, { limit: 4 });
  while (last) {
    const { items: newItems, last: newLast } = await libDB.fetch(
      {},
      { limit: 2, last: last }
    );

    last = newLast;

    items = [...items, ...newItems];
  }

  res.status(200).json({ error: false, data: items });
});

// add item to library
libraryRouter.put("/", async (req, res) => {
  const data = req.body as Omit<LibraryMangaProps, "key">;

  const r = await libDB.put(data);

  res.status(200).json({ error: false, data: r });
});

//
libraryRouter.get("/i/:itemKey", async (req, res) => {
  const { itemKey } = req.params;

  const r = await libDB.get(itemKey);
  if (r == null) {
    res.status(404).json({
      error: true,
      message: "Item key does not exist in your library.",
    });
    return;
  }

  res.json({ error: false, data: r });
});

libraryRouter.post("/i/:itemKey", async (req, res) => {});

export { libraryRouter };
