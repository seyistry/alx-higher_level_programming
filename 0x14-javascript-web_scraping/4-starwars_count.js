#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const id = 18;
let count = 0;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  // console.log('statusCode:', response && response.statusCode);
  const data = JSON.parse(body);
  for (const i in data.results) {
    // console.log(data.results[i]);
    for (const j in data.results[i].characters) {
      // console.log(data.results[i].characters[j]);
      if (
        data.results[i].characters[j] ==
        `https://swapi-api.alx-tools.com/api/people/${id}/`
      ) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
