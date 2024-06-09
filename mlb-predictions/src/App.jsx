import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import UpcomingGames from './components/UpcomingGames';
import Footer from './components/Footer';

const appStyle = {
  display: 'flex',
  flexDirection: 'column',
  minHeight: '100vh',
  backgroundColor: '#121212',
};

const contentWrapperStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  width: '100%',
  flexGrow: 1,
};

const heroWrapperStyle = {
  width: '100%',
};

const gamesWrapperStyle = {
  width: '100%',
  flexGrow: 1,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  padding: '2rem 0',
};

const App = () => {
  return (
    <div style={appStyle}>
      <Navbar />
      <div style={contentWrapperStyle}>
        <div style={heroWrapperStyle}>
          <Hero />
        </div>
        <div style={gamesWrapperStyle}>
          <UpcomingGames />
        </div>
        <Footer />
      </div>
    </div>
  );
};

export default App;
