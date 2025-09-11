const http = require('http');

// Every time someone visits your website (makes an HTTP request), the function (req, res) => { } gets called.
const app = http.createServer((req, res) => {
    // What this means: "I'm about to send a successful response containing plain text"
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    // What happens: The browser receives "Hello, World!" as the response.
    res.end('Hello, World!\n');
});

// define the PORT = Like a doorway on your computer where network traffic comes in
const PORT = 1245;

app.listen(PORT, 'localhost', () => {
  console.log("Hello Holberton School!");
});

module.exports = app;