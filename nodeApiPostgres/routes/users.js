const express = require('express')
const router = express.Router()

const { pool } = require('../config')


router.get('/', (request, response) => {
	pool.query('SELECT * FROM users ORDER BY id ASC', (error, data) => {
		if (error) {
			throw error;
		}

		response.status(200).json(data.rows);
	});
});


router.get('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
    	'SELECT * FROM users WHERE id = $1',
    	[id], (error, data) => {

    	if (error) throw error;

    	response.status(200).json(data.rows);
	});
});


router.post('/', (request, response) => {
	const { name, email } = request.body

	pool.query(
		'INSERT INTO users (name, email) VALUES ($1, $2)',
		[name, email], (error, data) => {
		if (error) throw error;

		response.status(201)
			.send(`User added with ID: ${data.insertId}`)
	});
});


router.put('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	const { name, email } = request.body

	pool.query(
		'UPDATE users SET name = $1, email = $2 WHERE id = $3',
		[name, email, id], (error, data) => {

		if (error) throw error;

		response.status(200).send(`User modified with ID: ${id}`)
	});
});


router.delete('/:id', (request, response) => {
	const id = parseInt(request.params.id)
	pool.query(
		'DELETE FROM users WHERE id = $1',
		[id], (error, data) => {

		if (error) throw error

		response.status(200).send(`User deleted with ID: ${id}`)
	});
});



module.exports = router
