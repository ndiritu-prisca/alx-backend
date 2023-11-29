import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value for a given school in Redis
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(`${value}`);
  } catch (error) {
    console.log(error);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
