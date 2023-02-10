#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;
const filePath = args[3];
const url = args[2];
const writableStream = fs.createWriteStream(filePath, 'utf-8');
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  writableStream.write(body);
});
