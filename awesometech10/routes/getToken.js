var express = require('express');
var router = express.Router();
var axios = require('axios');

/* GET token listing. */
router.get('/', function(req, res, next) {
  axios.get('https://quickauth.alles.cx?redirect=https://localhost:3000').then((res) => console.log(res))
});

module.exports = router;
