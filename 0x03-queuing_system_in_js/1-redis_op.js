import redis from 'redis';

// Create a new Redis client
const client = redis.createClient();

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
 * @param {string} schoolName - The name of the school which serves as the key.
 * @param {string} value - The value to set for the school.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Display the value of a school from the Redis database.
 *
 * @param {string} schoolName - The name of the school.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) throw err;
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
