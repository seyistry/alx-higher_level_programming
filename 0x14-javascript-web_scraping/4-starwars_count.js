#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
let count = 0;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  for (const i in data.results) {
    for (const j in data.results[i].characters) {
      if (data.results[i].characters[j].includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
