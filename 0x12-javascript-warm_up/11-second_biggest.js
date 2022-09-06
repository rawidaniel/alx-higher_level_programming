#!/usr/bin/node
const args = process.argv;
const val = 0;
if (!args[2] || parseInt(args[2]) === 1) {
  console.log(val);
} else {
  const newArray = args.sort();
  newArray.pop();
  console.log(newArray.pop());
}
