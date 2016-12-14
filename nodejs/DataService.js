var express = require('express'),
    pandaweb = require('./routes/pandawebdb'),
     cors = require('cors');

var app = express();
app.use(cors({origin: 'null'})); //If you use the frontend without any port on local pc just use null, use * to allow all

app.get('/pandaweb/all', pandaweb.findAll)
app.get('/pandaweb/range/:from/:to', pandaweb.findByRange);
//app.get('/pandaweb/:id', pandaweb.findById);
//app.post('/pandaweb', pandaweb.add;
//app.put('/pandaweb/:id', pandaweb.update);
app.delete('/pandaweb/delete/:id', pandaweb.delete);

app.listen(3000);
console.log('Listening on port 3000...');
