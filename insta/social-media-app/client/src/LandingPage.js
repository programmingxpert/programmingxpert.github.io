import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div>
      <h1>Welcome to Our Social Media App!</h1>
      <p>Connect with friends and start chatting.</p>
      <Link to="/dashboard">Go to Dashboard</Link>
    </div>
  );
};

export default LandingPage;
