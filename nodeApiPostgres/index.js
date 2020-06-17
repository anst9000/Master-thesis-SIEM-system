const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors')

const app = express();
const PORT = 3000;


/* MIDDLEWARE */
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));
app.use(cors());


/* ROUTES */
const syslogs = require('./routes/syslogs')
app.use('/syslogs', syslogs)

const pglogs = require('./routes/pglogs')
app.use('/pglogs', pglogs)

const mqttlogs = require('./routes/mqttlogs')
app.use('/mqttlogs', mqttlogs)

app.get('/', (request, response) => {
	response.json({
		info: 'Node.js, Express, and Postgres API'
	});
});




app.listen(PORT, () => {
	console.log(`Server listening on port ${PORT}`);
});
