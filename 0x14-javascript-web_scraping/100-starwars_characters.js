#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  for (const i in data.characters) {
    getName(data.characters[i]);
  }
});

const getName = (url) => {
  request(url, (error, response, body) => {
    if (error) console.error('error:', error);
    const data = JSON.parse(body);
    console.log(data.name);
  });
};
