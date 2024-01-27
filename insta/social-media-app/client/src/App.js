// App.js

import React from 'react';
import './App.css';
import LandingPage from './LandingPage';
import Dashboard from './Dashboard'; // Import the Dashboard component
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={LandingPage} />
          <Route path="/dashboard" component={Dashboard} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
