import * as express from "express";
import * as cors from "cors";
import { libraryRouter } from "./routers/library";

const app = express();

const port = process.env.PORT ?? "8080";

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("magna.lit internal api");
});

app.use("/library", libraryRouter);

app.listen(port, () => {
  console.log("Internal API is running at http://localhost:8080");
});
