// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('should return 4 when a=1 and b=3', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round b correctly (1 + 3.7 = 5)', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round a correctly (1.2 + 3.7 = 5)', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round both correctly (1.5 + 3.7 = 6)', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
