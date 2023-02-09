#!/usr/bin/env node

const fs = require('fs');
const args = process.argv;
const filePath = args[2];
const readableStream = fs.createReadStream(filePath, 'utf8');
readableStream.on('error', (error) => console.log(`error: ${error.message}`));
readableStream.on('data', (chunk) => console.log(chunk));
