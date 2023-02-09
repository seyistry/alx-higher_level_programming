#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
