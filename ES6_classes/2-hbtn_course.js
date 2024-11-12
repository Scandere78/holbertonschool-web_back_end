class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter pour 'name'
  get name() {
    return this._name;
  }

  // Setter pour 'name'
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;  // Utiliser '_name' au lieu de 'this.name'
  }

  // Getter pour 'length'
  get length() {
    return this._length;
  }

  // Setter pour 'length'
  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;  // Utiliser '_length' au lieu de 'this.length'
  }

  // Getter pour 'students'
  get students() {
    return this._students;
  }

  // Setter pour 'students'
  set students(value) {
    if (!Array.isArray(value) || value.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;  // Utiliser '_students' au lieu de 'this.students'
  }
}

export default HolbertonCourse;
