#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((element) => {
      element.characters.forEach((ele) => {
        if (ele.includes('18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
