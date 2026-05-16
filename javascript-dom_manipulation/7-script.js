#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        for (let i = 0; i < data.results.length; i++) {
            const li = document.createElement('li');
            li.textContent = data.results[i]['title'];
            document.querySelector('#list_movies').appendChild(li);
        }
    });