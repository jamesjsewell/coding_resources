
const express = require("express"),
createItemCont = require("./controllers/item.js"),
itemRoutes = express.Router()

itemRoutes.post("/items", createItemCont.post)
itemRoutes.get("/item/:id", createItemCont.get)
itemRoutes.get("/items", createItemCont.get)

module.exports = itemRoutes
