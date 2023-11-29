import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`)
});

client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (_channel, message) => {
  console.log(`${message}`);

  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
