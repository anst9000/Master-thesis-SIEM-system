const express = require('express')
const router = express.Router()

const { pool } = require('../config')


router.get('/', (request, response) => {
	pool.query('SELECT * FROM postgresprimary', (error, data) => {
		if (error) {
			throw error;
		}

		response.status(200).json(data.rows);
	});
});


router.get('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
    	'SELECT * FROM postgresprimary WHERE id = $1',
    	[id], (error, data) => {

    	if (error) throw error;

    	response.status(200).json(data.rows);
	});
});


router.post('/', (request, response) => {
	const { month, day, time, owner, process, pid, message } = request.body

	pool.query('INSERT INTO postgresprimary (date_time, host, port, owner, database, pid, message) VALUES ($1, $2, $3, $4, $5, $6, $7)',
		[date_time, host, port, owner, database, pid, message], (error, data) => {
		if (error) throw error;

		response.status(201)
			.send(`Postgreslog message added with ID: ${data.insertId}`)
	});
});


router.put('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	const { date_time, host, port, owner, database, pid, message } = request.body

	pool.query(
		'UPDATE postgresprimary SET date_time = $1, host = $2, port = $3, owner = $4, database = $5, pid = $6,message = $7, WHERE id = $8',
		[date_time, host, port, owner, database, pid, message, id], (error, data) => {

		if (error) throw error;

		response.status(200).send(`Postgreslog message modified with ID: ${id}`)
	});
});


router.delete('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
		'DELETE FROM postgreslogprimary WHERE id = $1',
		[id], (error, data) => {

		if (error) throw error

		response.status(200).send(`Postgreslog message deleted with ID: ${id}`)
	});
});



module.exports = router
