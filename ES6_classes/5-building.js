/* eslint-disable no-underscore-dangle */
export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('Cannot instantiate an abstract class');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  // eslint-disable-next-line class-methods-use-this
  get evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
