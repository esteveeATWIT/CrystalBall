// server.js
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const port = 4000;

// Allow all origins
app.use(cors());

app.get('/api/games', async (req, res) => {
  const date = req.query.date;

  if (!date) {
    return res.status(400).json({ error: 'Date parameter is required' });
  }

  try {
    console.log(`Fetching games for date: ${date}`);
    
    // Make the API request
    const response = await axios.get(`https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/${date}`, {
      headers: {
        'Ocp-Apim-Subscription-Key': '199bff5d93b34e8f88c848dcfe06d905', // Replace with your actual API key
      },
    });

    console.log('Response data:', response.data);

    res.json(response.data);
  } catch (error) {
    console.error('Error fetching games:', error.message);

    if (error.response) {
      console.error('Response data:', error.response.data);
      res.status(error.response.status).json({ error: error.response.data });
    } else if (error.request) {
      console.error('No response received:', error.request);
      res.status(500).json({ error: 'No response from API' });
    } else {
      console.error('Error:', error.message);
      res.status(500).json({ error: error.message });
    }
  }
});

app.listen(port, () => {
  console.log(`Proxy server running at http://localhost:${port}`);
});
