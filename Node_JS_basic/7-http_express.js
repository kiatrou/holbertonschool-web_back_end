const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

const filename = process.argv[2];

app.get('/', (req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
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
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;