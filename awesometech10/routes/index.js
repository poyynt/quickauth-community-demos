var express = require('express');
var router = express.Router();
var axios = require("axios");

/* GET home page. */
router.get('/', function(req, res, next) {
  let token = req.query.token;
  let name = '';
  console.log(token)
  if (req.query.token !== null) {
    axios.post("https://quickauth.alles.cx", {
      token: encodeURIComponent(token),
      redirect: 'https://allesauth.trevorthalacker.me'
    }).then((res) => {
      axios.get(`https://horizon.alles.cc/users/${res.data.id}`).then((res) => {
        name = res.data.name;
      })
    }).catch((err) => console.log(err));
  }
  setTimeout(() => res.send('Hello, ' + name), 5000)
});

module.exports = router;
