#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const obj = {};
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  for (const i in data) {
    if (data[i].completed === true) {
      if (data[i].userId in obj) {
        obj[data[i].userId] = obj[data[i].userId] + 1;
      } else {
        obj[data[i].userId] = 1;
      }
    }
  }
  console.log(obj);
});
