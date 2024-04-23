#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const WEDGE_ANTILLES_ID = '18';

function countWedgeAntillesMovies (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }

    const films = JSON.parse(body).results;

    const wedgeAntillesMovies = films.filter(film =>
      film.characters.includes(`https://swapi-alx.alx-tools.com/api/people/${WEDGE_ANTILLES_ID}/`)
    );

    console.log(wedgeAntillesMovies.length);
  });
}
