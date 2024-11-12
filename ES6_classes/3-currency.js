export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  get code() {
    return this.code;
  }

  set code(value) {
    this.code = value;
  }

  get name() {
    return this.name;
  }

  set name(value) {
    this.name = value;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
