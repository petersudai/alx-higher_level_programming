#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    const completedTasksByUser = tasks.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});

    console.log(completedTasksByUser);
  } else {
    console.error(error);
  }
});
