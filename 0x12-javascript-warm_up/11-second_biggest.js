#!/usr/bin/node
const args = process.argv;
const val = 0;
if (!args[2] || args.length === 3) {
  console.log(val);
} else {
  args.splice(0, 2);
  args.sort();
  console.log(args[args.length - 2]);
}
