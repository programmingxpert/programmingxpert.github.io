import React from 'react';
import './App.css';
import LandingPage from './LandingPage';
import Dashboard from './Dashboard'; // Import the Dashboard component
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; // Import BrowserRouter

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={LandingPage} />
        <Route path="/dashboard" component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;
