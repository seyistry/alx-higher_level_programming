#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  // console.log('statusCode:', response && response.statusCode);
  const data = JSON.parse(body);
  console.log(data.title);
});
