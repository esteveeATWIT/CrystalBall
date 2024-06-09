// src/components/Hero.jsx
import React from 'react';

const heroStyle = {
  height: '50vh', // Take up half the viewport height
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  textAlign: 'center',
  color: 'white',
  backgroundColor: '#444',
  margin: 0,
  padding: 0,
};

const textContainerStyle = {
  background: 'rgba(0, 0, 0, 0.5)', // Semi-transparent background for better text visibility
  padding: '20px',
  borderRadius: '8px',
};

const headingStyle = {
  fontSize: '3rem',
  marginBottom: '1rem',
};

const subHeadingStyle = {
  fontSize: '1.5rem',
};

const Hero = () => {
  return (
    <header style={heroStyle}>
      <div style={textContainerStyle}>
        <h1 style={headingStyle}>Welcome to MLB Game Predictions</h1>
        <p style={subHeadingStyle}>Predicting the outcomes of MLB games with our advanced algorithm.</p>
      </div>
    </header>
  );
};

export default Hero;
