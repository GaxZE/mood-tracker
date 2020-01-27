const db = require("../db");
const { Schema } = require("mongoose");

const EntrySchema = new Schema({
  _id: { type: Schema.ObjectId, auto: true, alias: "id" },
  date: { type: Date, default: Date.now },
  comment: String
});
