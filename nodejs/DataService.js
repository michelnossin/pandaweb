var express = require('express'),
    pandaweb = require('./routes/pandawebdb'),
     cors = require('cors'),
       path = require('path');


var app = express();
app.use(cors({origin: 'null'})); //If you use the frontend without any port on local pc just use null, use * to allow all
app.use(express.static(__dirname + '/..')); //All files in index.html are 1 directory above nodejs subdir

//Backend url's. Rest API
app.get('/pandaweb/all', pandaweb.findAll)
app.get('/pandaweb/range/:from/:to', pandaweb.findByRange);
app.delete('/pandaweb/delete/:id', pandaweb.delete);

// frontend url: http://localhost:3000
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/../index.html'));
});

//Backend url's todo later on
//app.get('/pandaweb/:id', pandaweb.findById);
//app.post('/pandaweb', pandaweb.add;
//app.put('/pandaweb/:id', pandaweb.update);

app.listen(3000);
console.log('Listening on port 3000...');
