import React from 'react';

const sectionStyle = {
  width: '80%',
  margin: 'auto',
  padding: '2rem',
  backgroundColor: '#1e1e1e',
  borderRadius: '8px',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
};

const headingStyle = {
  fontSize: '2rem',
  marginBottom: '1rem',
  textAlign: 'center',
  color: 'white',
};

const tableStyle = {
  width: '100%',
  borderCollapse: 'collapse',
  backgroundColor: '#333',
  color: '#fff',
};

const thStyle = {
  padding: '12px 15px',
  border: '1px solid #444',
  textAlign: 'left',
  fontSize: '1.2rem',
};

const tdStyle = {
  padding: '10px 15px',
  border: '1px solid #444',
  textAlign: 'left',
  fontSize: '1rem',
};

const UpcomingGames = () => {
  return (
    <section style={sectionStyle}>
      <h2 style={headingStyle}>Upcoming Games</h2>
      <table style={tableStyle}>
        <thead>
          <tr>
            <th style={thStyle}>Date</th>
            <th style={thStyle}>Team 1</th>
            <th style={thStyle}>Team 2</th>
            <th style={thStyle}>Prediction</th>
            <th style={thStyle}>Result</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style={tdStyle}>2024-06-04</td>
            <td style={tdStyle}>Red Sox</td>
            <td style={tdStyle}>Yankees</td>
            <td style={tdStyle}>65.50%</td>
            <td style={tdStyle}>3-2</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
};

export default UpcomingGames;
