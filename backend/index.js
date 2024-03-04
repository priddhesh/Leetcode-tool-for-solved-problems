require('dotenv').config();
const express = require('express');
const mysql = require('mysql');
const cors = require('cors');


const app = express();
app.use(express.json());

const corsOptions = {
    origin: "https://leetcode-solved-problems-tracker.onrender.com", 
    methods: ['GET', 'POST'], 
    allowedHeaders: ['Content-Type', 'Authorization'] 
  };
  
  app.use(cors(corsOptions));

const pool = mysql.createPool({
  host: process.env.HOST,
  user: process.env.USER,
  password: process.env.PASSWORD,
  database: process.env.DB,
  port: process.env.PORT,
});

app.get('/ques', (req, res) => {
  pool.getConnection((err, connection) => {
    if (err) {
      console.error('Error getting connection from pool:', err);
      res.status(500).json({ error: 'Internal server error' });
      return;
    }

    connection.query('SELECT * FROM solvedques', (error, results, fields) => {
      connection.release(); 

      if (error) {
        console.error('Error executing query:', error);
        res.status(500).json({ error: 'Internal server error' });
        return;
      }
      res.json(results);
    });
  });
});

app.post('/updateStatus/:ques', (req, res) => {
    const {status} = req.body;
    const ques = req.params.ques;
    console.log(status,ques);
  
    pool.getConnection((err, connection) => {
      if (err) {
        console.error('Error getting connection from pool:', err);
        res.status(500).json({ error: 'Internal server error' });
        return;
      }
  
      connection.query('UPDATE solvedques SET status = ? WHERE ques = ?', [status, ques], (error, results, fields) => {
        connection.release(); 
  
        if (error) {
          console.error('Error executing query:', error);
          res.status(500).json({ error: 'Internal server error' });
          return;
        }
  
        res.json({ message: 'Status updated successfully' });
      });
    });
  });

  
const PORT =  3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
