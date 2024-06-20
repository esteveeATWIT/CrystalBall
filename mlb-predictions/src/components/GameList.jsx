// src/components/GameList.jsx
import React, { useEffect, useState } from 'react';
import GameCard from './GameCard';

const GameList = () => {
  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const today = new Date().toISOString().split('T')[0];
        const response = await fetch(`https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/${today}?key=${import.meta.env.VITE_API_KEY}`);
        
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log('API Data:', data);  // Debugging

        if (!Array.isArray(data)) {
          throw new Error('Unexpected API response format');
        }
        setGames(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchGames();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="game-list">
      {games.length > 0 ? (
        games.map((game) => (
          <GameCard key={game.GameID} game={game} />
        ))
      ) : (
        <p>No games found for today.</p>
      )}
    </div>
  );
};

export default GameList;
