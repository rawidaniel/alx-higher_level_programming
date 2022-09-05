#!/usr/bin/node
const args = parseInt(process.argv[2]);

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    let character = '';
    for (let j = 0; j < args; j++) {
      character += 'X';
    }
    console.log(character);
  }
}
