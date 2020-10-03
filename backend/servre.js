
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = 3000;

var router = express.Router();

router.get('/', function(req, res, next){
    res.json([
        
    ])
})

app.use("/", express.static("public"));
app.use("/", express.static(__dirname + "/public"));


git 
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
