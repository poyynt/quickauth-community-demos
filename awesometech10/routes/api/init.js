var express = require('express');
var router = express.Router();

/* GET api shit */
router.get('/', function(req, res, next) {
    res.redirect('https://quickauth.alles.cx?redirect=https://allesauth.trevorthalacker.me')
});

module.exports = router;
