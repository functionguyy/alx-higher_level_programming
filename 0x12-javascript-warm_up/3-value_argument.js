#!/usr/bin/node

const { argv } = require('process');

let i = 0;
const noArg = 'No argument';

while (argv[i] !== undefined) {
  i++;
}

if (i > 1) {
  console.log(argv[2]);
} else {
  console.log(noArg);
}
