#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const task = JSON.parse(body);
    const dict = task.reduce(function (acc, ele) {
      if (!acc[ele.userId]) {
        if (ele.completed) {
          acc[ele.userId] = 1;
        }
      } else {
        if (ele.completed) {
          acc[ele.userId] += 1;
        }
      }
      return acc;
    }, {});
    console.log(dict);
  }
});
