#!/usr/bin/node
const args = process.argv;
const val = 0;
if (!args[2] || parseInt(args[2]) === 1) {
  console.log(val);
} else {
  let first_max = 0;
  let second_max = 0;
  for (const i of args) {
    if (i > first_max) {
      first_max = i;
    }
  }
  for (const i of args) {
    if (i > second_max && i !== first_max) {
      second_max = i;
    }
  }
}
