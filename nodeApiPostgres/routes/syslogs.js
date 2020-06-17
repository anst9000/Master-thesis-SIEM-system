const express = require('express')
const router = express.Router()

const { pool } = require('../config')


router.get('/', (request, response) => {
	pool.query('SELECT * FROM syslogprimary', (error, data) => {
		if (error) {
			throw error;
		}

		response.status(200).json(data.rows);
	});
});


router.get('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
    	'SELECT * FROM syslogprimary WHERE id = $1',
    	[id], (error, data) => {

    	if (error) throw error;

    	response.status(200).json(data.rows);
	});
});


router.post('/', (request, response) => {
	const { month, day, time, owner, process, pid, message } = request.body

	pool.query('INSERT INTO syslogprimary (month, day, time, owner, process, pid, message) VALUES ($1, $2, $3, $4, $5, $6, $7)',
		[month, day, time, owner, process, pid, message], (error, data) => {
		if (error) throw error;

		response.status(201)
			.send(`Syslog message added with ID: ${data.insertId}`)
	});
});


router.put('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	const { month, day, time, owner, process, pid, message } = request.body

	pool.query(
		'UPDATE syslogprimary SET month = $1, day = $2, time = $3, owner = $4, process = $5, pid = $6,message = $7, WHERE id = $8',
		[month, day, time, owner, process, pid, message, id], (error, data) => {

		if (error) throw error;

		response.status(200).send(`Syslog message modified with ID: ${id}`)
	});
});


router.delete('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
		'DELETE FROM syslogprimary WHERE id = $1',
		[id], (error, data) => {

		if (error) throw error

		response.status(200).send(`Syslog message deleted with ID: ${id}`)
	});
});



module.exports = router
