import redis from 'redis';
import { promisify } from 'util';

// Create a new Redis client
const client = redis.createClient();

// Convert client.get to a function that returns a Promise
const getAsync = promisify(client.get).bind(client);

// Log a message when the client successfully connects to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log an error message if the client fails to connect to the Redis server
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
}); 

/**
 * Set a new school in the Redis database.
 *
 * @param {string} schoolName - The name of the school.
 * @param {string} value - The value to set for the school.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Display the value of a school from the Redis database.
 * This function uses async/await to wait for the Promise returned by getAsync to resolve.
 *
 * @param {string} schoolName - The name of the school.
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

// Display the value of 'Holberton' from the Redis database
displaySchoolValue('Holberton');

// Set a new school 'HolbertonSanFrancisco' in the Redis database with a value of '100'
setNewSchool('HolbertonSanFrancisco', '100');

// Display the value of 'HolbertonSanFrancisco' from the Redis database
displaySchoolValue('HolbertonSanFrancisco');
