const express = require("express"),
	bodyParser = require("body-parser"),
	path = require("path")

// runs express app and sets defined port
var app = express()
const PORT = process.env.PORT || 3000
app.set("port", PORT)


// middleware, transforms http request so that you can use req.body json format 
// for accepting json data from http requests
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.static(path.join(__dirname, '../public') ))
//to use more directories for serving assets
//app.use(express.static('files'))

// starts the app listening for requests
app.listen(PORT, function () {
	console.log(
		"\n\n===== listening for requests on port " + PORT + " =====\n\n"
	)
})

var views = { root: path.join(__dirname, '../public/views') }

//sends back terminal_info page html file
app.get("/terminal_info", terminal_info)
app.get("/", main_page)

function main_page(req, res, next){

	res.sendFile('main_page.html', views)

}

function terminal_info(req, res, next) {

	res.sendFile('terminal_info.html', views);

}






