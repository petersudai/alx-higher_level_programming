#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;
    const charactersPromises = charactersUrls.map(url => {
      return new Promise((resolve, reject) => {
        request(url, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(error || `Request failed with status code ${response.statusCode}`);
          }
        });
      });
    });
    Promise.all(charactersPromises)
      .then(characters => {
        characters.forEach(character => {
          console.log(character);
        });
      })
      .catch(error => {
        console.error(error);
      });
  } else {
    console.error(error || `Request failed with status code ${response.statusCode}`);
  }
});
