const express = require('express');
const hbs = require('hbs');
const path = require('path');
const PORT = 8123;

// const bodyParser = require('body-parser');
const app = express();

app.set('views',path.join(__dirname,'views'));
app.set('view engine','hbs');
// app.use(bodyParser.urlencoded({ extended: false }));

// li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

var fun = require('./exec');

app.get('/',(req,res) => {
  // li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  console.log("Game Page")
  res.render('gamePage',{
        list : fun.startFunction(),
        score: 0
  });
});

app.post('/left', fun.leftCheck)
app.post('/up', fun.upCheck)
app.post('/down', fun.downCheck)
app.post('/right', fun.rightCheck)

app.listen(PORT,() => {
  console.log('Server is running at port '+PORT);
})
