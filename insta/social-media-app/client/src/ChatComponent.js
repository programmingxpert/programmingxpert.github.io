import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const ChatComponent = () => {
  const [message, setMessage] = useState('');
  const [receivedMessage, setReceivedMessage] = useState('');
  const [receiverId, setReceiverId] = useState(''); // Added state for receiver ID

  const socket = io('http://localhost:3001');

  useEffect(() => {
    socket.on('private_message', (data) => {
      setReceivedMessage(data.message); // Update received message
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    socket.emit('private_message', { receiverId, message });
    setMessage('');
  };

  return (
    <div>
      <div>{receivedMessage}</div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <input
        type="text"
        placeholder="Receiver ID"
        value={receiverId}
        onChange={(e) => setReceiverId(e.target.value)}
      />
      <button onClick={sendMessage}>Send Message</button>
    </div>
  );
};

export default ChatComponent;
