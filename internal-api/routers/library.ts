import { Router } from "express";
import { libDB } from "../lib/base";

const libraryRouter = Router();

// fetch items from library
libraryRouter.get("/", async (req, res) => {
  let { items, last } = await libDB.fetch({}, { limit: 2 });
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

libraryRouter.put("/", async (req, res) => {});

libraryRouter.get("/i/:itemKey", async (req, res) => {});

libraryRouter.post("/i/:itemKey", async (req, res) => {});

export { libraryRouter };
