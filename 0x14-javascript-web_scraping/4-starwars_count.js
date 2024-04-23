#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
	  const characterID = '18';

	  const filteredMovies = films.filter(movie => movie.characters.some(character => character.endsWith(characterId)));

	  console.log(filteredMovies.length);
  } else {
	  console.error(error);
  }
});
