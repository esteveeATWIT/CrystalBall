// src/components/Footer.jsx
import React from 'react';

const footerStyle = {
  textAlign: 'center',
  padding: '1rem',
  backgroundColor: '#333',
  color: '#fff',
  width: '100%',
  position: 'relative',
  bottom: 0,
  boxSizing: 'border-box',
};

const Footer = () => {
  return (
    <footer style={footerStyle}>
      <p>&copy; 2024 MLB Game Predictions. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
