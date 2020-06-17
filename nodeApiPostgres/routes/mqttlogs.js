const express = require('express')
const router = express.Router()

const { pool } = require('../config')


router.get('/', (request, response) => {
	pool.query('SELECT * FROM mqttprimary', (error, data) => {
		if (error) {
			throw error;
		}

		response.status(200).json(data.rows);
	});
});


router.get('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
    	'SELECT * FROM mqttprimary WHERE id = $1',
    	[id], (error, data) => {

    	if (error) throw error;

    	response.status(200).json(data.rows);
	});
});


router.post('/', (request, response) => {
	const { date_time, message } = request.body

	pool.query('INSERT INTO mqttprimary (date_time, message) VALUES ($1, $2)',
		[date_time, message], (error, data) => {
		if (error) throw error;

		response.status(201)
			.send(`MQTTlog message added with ID: ${data.insertId}`)
	});
});


router.put('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	const { date_time, message } = request.body

	pool.query(
		'UPDATE mqttprimary SET date_time = $1, message = $2, WHERE id = $3',
		[date_time, message, id], (error, data) => {

		if (error) throw error;

		response.status(200).send(`MQTTlog message modified with ID: ${id}`)
	});
});


router.delete('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
		'DELETE FROM mqttprimary WHERE id = $1',
		[id], (error, data) => {

		if (error) throw error

		response.status(200).send(`MQTTlog message deleted with ID: ${id}`)
	});
});



module.exports = router
