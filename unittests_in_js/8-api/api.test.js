const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('./api'); // ton app Express

chai.use(chaiHttp);
const { expect } = chai;

describe('Index page', () => {
  it('should return correct status code and result', (done) => {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(err).to.be.null;
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
