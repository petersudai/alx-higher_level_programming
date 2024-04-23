#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

function countWedgeAntillesMovies(apiUrl) {
	request(apiUrl, (error, response, body) => {
		if (error) {
			console.error('Error:', error);
			return;
		}

		const films = JSON.parse(body).results;

		const wedgeAntillesMovies = films.filter(film =>
			film.characters.includes('https://swapi-alx.alx-tools.com/api/people/18/')
		);

		console.log(wedgeAntillesMovies.length);
	});
}

countWedgeAntillesMovies(apiUrl);
