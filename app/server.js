const express = require('express');
const mongoose = require('mongoose');
const session = require('express-session');

mongoose.connect('mongodb+srv://Puski:satya%40123@cluster0.quz6u.mongodb.net', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const userSchema = new mongoose.Schema({
  username: String,
  password: String,
});

const User = mongoose.model('User', userSchema);

const app = express();

app.use(session({
  secret: 'your-secret-key',
  resave: true,
  saveUninitialized: true
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  const username = req.session.username;

  if (username) {
    res.sendFile(__dirname + '/chatpage.html');
  } else {
    res.redirect('/login');
  }
});

app.get('/login', (req, res) => {
  const message = req.session.message;
  req.session.message = '';

  res.write(`
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
            }

            .container {
                margin: 100px auto;
                max-width: 400px;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            h2 {
                margin-bottom: 20px;
            }

            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }

            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h2>Login</h2>
            <div id="message">${message ? `<p>${message}</p>` : ''}</div>
            <form action="/login" method="POST">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Login">
            </form>
        </div>
        <script>
            setTimeout(function(){
                window.location.href = 'chatpage.html';
            }, 3000);
        </script>
    </body>

    </html>
  `);
  res.end();
});
app.use(express.static(__dirname));

app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const existingUser = await User.findOne({ username });

    if (existingUser) {
      req.session.message = 'User already exists';
    } else {
      const user = new User({ username, password });
      await user.save();
      req.session.username = username;
      req.session.message = 'User saved successfully';
    }
  } catch (error) {
    console.error(error);
    req.session.message = 'Error saving user';
  }

  res.redirect('/');
});

app.listen(3000, () => {
  console.log('Server started on http://localhost:3000');
});
