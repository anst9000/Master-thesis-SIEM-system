require('dotenv').config()
const { db_user, db_pass, db_host, db_port, db_base } = require('./keys')

const { Pool } = require('pg')
const isProduction = process.env.NODE_ENV === 'production'

const connectionString =
	`postgresql://${db_user}:${db_pass}@${db_host}:${db_port}/${db_base}`

const pool = new Pool({
	connectionString: isProduction ? process.env.DATABASE_URL : connectionString,
	ssl: isProduction,
})

module.exports = { pool }
