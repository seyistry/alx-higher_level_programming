#!/usr/bin/node

const request = require('request');
const fetch = require('node-fetch');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  getName(data.characters);
});

const getName = async (data) => {
  for (const url of data) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data.name);
  }

  // request(url, (error, response, body) => {
  //   if (error) console.error('error:', error);
  //   const data = JSON.parse(body);
  //   console.log(data.name);
  // });
};
