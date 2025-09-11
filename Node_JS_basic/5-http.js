const http = require('http');
const fs = require('fs');

const host = 'localhost';
const port = 1245;

const filename = process.argv[2];

async function requestListener(req, res) {
  switch (req.url) {
    case '/students':
      res.writeHead(200);

      try {
        res.write('This is the list of our students\n');

        const data = await fs.readFileSync(filename, 'utf-8');
        const rows = data.split('\n').slice(1);

        const studentsCS = [];
        const studentsSWE = [];

        for (const row of rows) {
          if (row.trim() !== '') {
            const data = row.split(',');

            if (data[3] === 'CS') { // hardcode
              studentsCS.push(data[0]);
            }

            if (data[3] === 'SWE') { // hardcode
              studentsSWE.push(data[0]);
            }
          }
        }

        res.write(`Number of students: ${studentsCS.length + studentsSWE.length}\n`);
        res.write(`Number of students in CS: ${studentsCS.length}. List: ${studentsCS.join(', ')}\n`);
        res.end(`Number of students in SWE: ${studentsSWE.length}. List: ${studentsSWE.join(', ')}`);
      } catch (error) {
        res.end('Cannot load the database');
      }

      break;
    default:
      res.writeHead(200);
      res.end('Hello Holberton School!');
  }
}

const app = http.createServer(requestListener);
app.listen(port, host, () => {
  console.log(`Server is running on http://${host}:${port}`);
});

module.exports = app;