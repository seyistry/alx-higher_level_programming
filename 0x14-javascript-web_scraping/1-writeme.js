#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const filePath = args[2];
const content = args[3];
const writableStream = fs.createWriteStream(filePath, 'utf-8');
writableStream.write(content);
