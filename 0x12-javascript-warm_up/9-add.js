#!/usr/bin/node
const args = process.argv;
const firstInteger = parseInt(args[2]);
const secondInteger = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstInteger, secondInteger);
