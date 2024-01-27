    const express = require('express');
    const router = express.Router();
    const User = require('./models/User');

    // Register endpoint
    router.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;
        const user = await User.create({ username, password });
        res.json({ user });
    } catch (error) {
        res.status(500).json({ error: 'Error registering user' });
    }
    });

    // Login endpoint
    router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        const user = await User.findOne({ username, password });
        if (!user) throw new Error('Invalid username or password');
        res.json({ user });
    } catch (error) {   
        res.status(401).json({ error: error.message });
    }
    });

    module.exports = router;
