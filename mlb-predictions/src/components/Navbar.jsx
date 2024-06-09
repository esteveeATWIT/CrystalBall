// src/components/Navbar.jsx
import React from 'react';

const navStyle = {
  width: '100%',
  backgroundColor: '#333',
  padding: '1rem',
  boxSizing: 'border-box',
  position: 'fixed',
  top: 0,
  left: 0,
  zIndex: 1000,
};

const navContainerStyle = {
  maxWidth: '1000px',
  margin: '0 auto',
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
};

const navLinksStyle = {
  listStyle: 'none',
  display: 'flex',
  gap: '1rem',
  padding: 0,
  margin: 0,
};

const linkStyle = {
  color: '#fff',
  textDecoration: 'none',
};

const logoStyle = {
  color: '#fff',
  fontSize: '1.5rem',
  textDecoration: 'none',
};

const Navbar = () => {
  return (
    <nav style={navStyle}>
      <div style={navContainerStyle}>
        <a href="#" style={logoStyle}>MLB Predictions</a>
        <ul style={navLinksStyle}>
          <li><a href="#home" style={linkStyle}>Home</a></li>
          <li><a href="#project" style={linkStyle}>Our Project</a></li>
          <li><a href="#about" style={linkStyle}>About Us</a></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
