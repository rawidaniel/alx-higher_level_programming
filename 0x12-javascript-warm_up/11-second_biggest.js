#!/usr/bin/node
const args = process.argv.slice(2);

function secondBiggestInteger (array) {
  if (array.length < 2) {
    return 0;
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return array.pop();
  }
}
console.log(secondBiggestInteger(args));
