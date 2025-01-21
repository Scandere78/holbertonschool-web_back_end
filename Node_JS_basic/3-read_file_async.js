const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Enlever l'entête
      const students = lines.slice(1);
      if (students.length === 0) {
        console.log('Number of students: 0');
        return;
      }

      console.log(`Number of students: ${students.length}`);

      const fields = {};
      for (const student of students) {
        const [firstname, , field] = student.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }

      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
