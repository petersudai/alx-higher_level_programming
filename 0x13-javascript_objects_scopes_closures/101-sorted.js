#!/usr/bin/node

const dict = require('./101-data.js').dict;

const sortedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!(occurrences in sortedDict)) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
