#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

const dataA = fs.readFileSync(fileA, 'utf8').trim();
const dataB = fs.readFileSync(fileB, 'utf8').trim();
const concatenatedData = dataA + '\n' + dataB;
fs.writeFileSync(destinationFile, concatenatedData);
