const dotenv = require('dotenv')
dotenv.config()

module.exports = {
	db_user: process.env.DB_USER,
	db_pass: process.env.DB_PASSWORD,
	db_host: process.env.DB_HOST,
	db_port: process.env.DB_PORT,
	db_base: process.env.DB_DATABASE,
};
