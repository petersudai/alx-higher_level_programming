#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.body);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((total, film) => {
      if (film.characters.includes(`${apiUrl}${characterId}/`)) {
        return total + 1;
      } else {
        return total;
      }
    }, 0);
    console.log(count);
  }
});
