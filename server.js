const express = require("express");
const bodyParser = require("body-parser");

var app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

app.get("/", () => {
  return console.log("Hello world");
});

app.listen(port, () => {
  console.log(`Started app on port ${port}`);
});

module.exports = {
  app
};
