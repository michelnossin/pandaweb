var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/pandawebdb');

Server = require("jsonrpc-node").HTTP.Server;

var server = new Server({
      echo:function(args, reply){
         console.log("lets echo " + args)
         return reply(args);
       },
       search_text:function(args, reply){
         var collection = db.get('pandawebcol');
          result = "No results founds"
          collection.find({}).then((docs) => {
              result = { message: 'Real data from mongodb!', datatable: docs };
              return reply(result);
          })
        }
      });

var express    = require('express');        // call express
var app        = express();                 // define our app using express

var backport = 3001
var frontport = 3000 //process.env.PORT || 3001;        // set our port
var router = express.Router();              // get an instance of the express Router

// more routes for our API will happen here
app.use("/app", function (req, res, next) {
  res.send('This is your frontend ');
});
app.use("/data", server); //use the jsonrpc

server.listen(backport, "localhost");
app.listen(frontport, "localhost");

console.log('Opening PandaWeb backend on port ' + backport);
console.log('Opening PandaWeb frontend on port ' + frontport);
