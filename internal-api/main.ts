import * as express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("magna.lit internal api");
});

app.listen(8080, () => {
  console.log("Internal API is running at http://localhost:8080");
});
