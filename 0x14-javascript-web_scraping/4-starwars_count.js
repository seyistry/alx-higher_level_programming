#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const id = 18;
let count = 0;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  for (const i in data.results) {
    for (const j in data.results[i].characters) {
      if (
        data.results[i].characters[j] ===
        `https://swapi-api.alx-tools.com/api/people/${id}/`
      ) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
