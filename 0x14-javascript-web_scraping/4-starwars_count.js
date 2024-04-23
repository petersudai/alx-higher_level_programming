#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.error(error || `Request failed with status code ${response.statusCode}`);
  }
});
