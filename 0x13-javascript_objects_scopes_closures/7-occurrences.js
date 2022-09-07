#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const value of list) {
    if (searchElement === value) {
      count++;
    }
  }
  return count;
};
