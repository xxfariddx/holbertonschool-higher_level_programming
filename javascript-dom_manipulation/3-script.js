#!/usr/bin/node

document.querySelector('#toggle_header').addEventListener('click', function() {
    document.querySelector('header').classList.toggle('red');
    document.querySelector('header').classList.toggle('green');
});