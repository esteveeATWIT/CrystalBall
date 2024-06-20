// src/components/GameCard.jsx
import React from 'react';
import teamNames from './teamNames';  // Adjusted import path

const gameCardStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: '1rem',
  border: '1px solid #ccc',
  marginBottom: '1rem',
  borderRadius: '5px',
  backgroundColor: '#f9f9f9',
};

const sectionStyle = {
  flex: 1,
  textAlign: 'center',
};

const GameCard = ({ game }) => {
  const homeTeamFullName = teamNames[game.HomeTeam];
  const awayTeamFullName = teamNames[game.AwayTeam];
  const prediction = ''; // Placeholder for prediction

  const getWinner = () => {
    if (game.Status === 'Final') {
      const homeTeamRuns = game.HomeTeamRuns;
      const awayTeamRuns = game.AwayTeamRuns;

      if (homeTeamRuns > awayTeamRuns) {
        return `${homeTeamFullName} Wins`;
      } else if (homeTeamRuns < awayTeamRuns) {
        return `${awayTeamFullName} Wins`;
      } else {
        return 'Tie Game';
      }
    } else {
      return 'To be determined';
    }
  };

  const getScore = () => {
    if (game.Status === 'Final') {
      return `${game.HomeTeamRuns} - ${game.AwayTeamRuns}`;
    } else {
      return '';
    }
  };

  return (
    <div style={gameCardStyle}>
      <div style={sectionStyle}>
        <h2>{homeTeamFullName} vs {awayTeamFullName}</h2>
        <p>Start Time: {new Date(game.DateTime).toLocaleTimeString()}</p>
      </div>
      <div style={sectionStyle}>
        <p>{prediction || 'Prediction'}</p>
      </div>
      <div style={sectionStyle}>
        <p>{getWinner()}</p>
        <p>{getScore()}</p>
      </div>
    </div>
  );
};

export default GameCard;
