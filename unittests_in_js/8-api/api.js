const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

module.exports = app;

// Seul lancement serveur indépendant
if (require.main === module) {
  const port = 7865;
  app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
  });
}
