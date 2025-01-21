const http = require('http');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    const studentData = lines.slice(1);

    const fields = {};
    studentData.forEach((line) => {
      const [firstname, , , field] = line.split(',');

      if (firstname && field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    const totalStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
    let response = `Number of students: ${totalStudents}\n`;

    for (const [field, students] of Object.entries(fields)) {
      response += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
    }

    return response;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  const { url } = req;

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (url === '/') {
    res.end('Hello Holberton School!\n');
  } else if (url === '/students') {
    const dbFile = process.argv[2];

    if (!dbFile) {
      res.end('Cannot load the database\n');
      return;
    }

    try {
      const studentsList = await countStudents(dbFile);
      res.end(`This is the list of our students\n${studentsList}`);
    } catch (error) {
      res.end('Cannot load the database\n');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found\n');
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
