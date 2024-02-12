#! /usr/bin/node

const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2/promise');
const session = require('express-session');

// create the Express app
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({ secret: 'secret key', resave: false, saveUninitialized: true }));

let db; // database connection

mysql.createConnection({
  host: "db",
  port: "3306",
  user: 'user',
  password: 'password',
  database: 'website'
}).then(connection => {
  db = connection;
  console.log('Connected to the database');
})
.catch(err => {
  console.error('Error connecting to the database...')
  console.error(err.stack)
});

app.listen(3000, () => console.log("Server started on port: " + 3000));


// app.post('/signup', async (req, res) => {
//   const [rows] = await db.execute('SELECT * FROM Users',
// [req.body.username]);

//   if(rows[0]) // user already exists
//     return res.status(409).send({ error: 'Username is taken' });

//   const [result] = await db.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)',
// [req.body.username, req.body.password]);

//   res.status(201).send({ message: 'User created successfully' });
// });


// app.post('/login', async (req, res) => {
//   const [rows] = await db.execute('SELECT * FROM Users WHERE Username = ? AND Password = ?',
// [req.body.username, req.body.password]);

//   if(!rows[0]) // user doesn't exist or wrong password
//     return res.status(401).send({ error: 'Invalid username or password' });

//   req.session.user = rows[0];
//   res.send({ message: 'Logged in successfully' });
// });
