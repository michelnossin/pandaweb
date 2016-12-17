var mongo = require('mongodb');
var ObjectID = require("mongodb").ObjectID;

var coll = 'pandawebcol'
var database = 'pandawebdb'
var port = 27017
var server = 'localhost'

var Server = mongo.Server,
    Db = mongo.Db,
    BSON = mongo.BSONPure;

var server = new Server(server, port, {auto_reconnect: true});
db = new Db(database, server);

db.open(function(err, db) {
    if(!err) {
        console.log("Connected to " + database + " database");
        db.collection(coll, {strict:true}, function(err, collection) {
            if (err) {
                console.log("The " + coll+ " collection doesn't exist. ...");
            }
        });
    }
});

//Get rows in a collections using given row numbers as range (rownumbers start at 0)
exports.findByRange = function(req, res) {
    var from_row= parseInt(req.params.from);
    var to_row= parseInt(req.params.to);
    db.collection(coll, function(err, collection) {
      collection.find().limit(to_row - from_row).skip(from_row).toArray(function(err, items) {
          res.send(items);
      });

    });
};

//Get all data in a collection
exports.findAll = function(req, res) {
    db.collection(coll, function(err, collection) {
        collection.find().toArray(function(err, items) {
            res.send(items);
        });
    });
};

//Remove a row from a collection using it's _id column
exports.delete = function(req, res) {
    var mid = req.params.id;
    console.log('Deleting id: ' + mid);
    db.collection(coll, function(err, collection) {
        collection.findOneAndDelete({ _id: ObjectID(mid) }, function (err, doc) {
            if (err) {
              console.log("Some error occured while deleting the row: " + err);
              res.send(doc)
            }
            else {
              console.log("Deleted row");
              res.send(doc)
            }
        });
    });
}
