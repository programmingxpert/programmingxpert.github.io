const express = require('express');
const mongoose = require('mongoose');
const routes = require('./routes');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const session = require('express-session');
const bcrypt = require('bcrypt');
const User = require('./models/User');
const http = require('http');
const io = require('socket.io')(http);
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3001;

mongoose.connect('mongodb+srv://Puski:satya%40123@cluster0.quz6u.mongodb.net', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.use(express.json());
app.use(session({
  secret: '123',
  resave: false,
  saveUninitialized: true
}));

app.use(passport.initialize());
app.use(passport.session());

// Configure local strategy for Passport
passport.use(new LocalStrategy((username, password, done) => {
  User.findOne({ username: username }, (err, user) => {
    if (err) return done(err);
    if (!user) return done(null, false, { message: 'Incorrect username.' });

    bcrypt.compare(password, user.password, (err, result) => {
      if (err) return done(err);
      if (!result) return done(null, false, { message: 'Incorrect password.' });

      return done(null, user);
    });
  });
}));

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.findById(id, (err, user) => {
    done(err, user);
  });
});

// Define your API routes
app.use('/api', routes);

// Set up socket.io
io.on('connection', (socket) => {
  console.log('A user connected');

  socket.on('disconnect', () => {
    console.log('User disconnected');
  });

  socket.on('private_message', (data) => {
    io.to(data.receiverId).emit('private_message', data.message);
  });
});

// Serve static files from the React app
app.use(express.static(path.join(__dirname, '../client/build')));

// Handle React routing, return all requests to React app
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/build', 'index.html'));
});

app.use('/api', routes);

// Start the server
const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
