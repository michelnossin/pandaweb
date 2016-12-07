var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/pandawebdb');

var cors = require('cors');
var express    = require('express');        // call express
var app        = express();                 // define our app using express
app.use(cors());

var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;        // set our port
var router = express.Router();              // get an instance of the express Router

//(accessed at GET http://localhost:8080/data)
router.get('/', function(req, res) {
      var db = req.db;
      var collection = db.get('pandawebcol');
      collection.find({},{},function(e,docs){
        res.json({ message: 'Real data from mongodb!',
                   datatable: docs });
      });

});

app.use(function(req,res,next){
    req.db = db;
    next();
});

// more routes for our API will happen here
app.use('/data', router);
app.listen(port);
console.log('Opening PandaWeb on port ' + port);
