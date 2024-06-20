// src/App.jsx
import React from 'react';
import GameList from './components/GameList';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Footer from './components/Footer';

const App = () => {
  return (
    <div>
      <Navbar />
      <Hero />
      <div style={{ paddingTop: '4rem', paddingBottom: '4rem' }}>
        <GameList />
      </div>
      <Footer />
    </div>
  );
};

export default App;
