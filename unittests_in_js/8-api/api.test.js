const request = require('supertest');
const app = require('./api');

describe('Index page', () => {
  it('should return correct status code and result', (done) => {
    request(app)
      .get('/')
      .expect(200)
      .expect('Welcome to the payment system', done);
  });
});