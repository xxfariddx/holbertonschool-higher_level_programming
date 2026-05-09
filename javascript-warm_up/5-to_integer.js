#!/usr/bin/node

const arg1 = process.argv[2];

const anInteger = parseInt(arg1);

if (isNaN(anInteger)) {
  console.log('Not a number');
} else {
  console.log('My number:', anInteger);
}
