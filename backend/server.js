const express = require("express"),
	bodyParser = require("body-parser"),
	path = require("path")

// runs express app and sets defined port
var app = express()
const PORT = process.env.PORT || 3000
app.set("port", PORT)

// middleware, transforms http request so that you can use req.body json format 
// for accepting json data from http requests if need be 
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

// serves static files
app.use(express.static(path.join(__dirname, '../public') ))

// starts the app listening for requests
app.listen(PORT, function () {
	console.log(
		"\n\n===== listening for requests on port " + PORT + " =====\n\n"
	)
})

var views = { root: path.join(__dirname, '../') }

app.get("/", main_page)

function main_page(req, res, next){

	res.sendFile('index.html', views)

}






