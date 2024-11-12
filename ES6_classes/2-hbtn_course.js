export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this.name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this.name = value;
  }

  get length() {
    return this.length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this.length = value;
  }

  get students() {
    return this.students;
  }

  set students(value) {
    if (!Array.isArray(value) || value.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this.students = value;
  }
}
