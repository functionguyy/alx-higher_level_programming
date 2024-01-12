#!/usr/bin/node

const { argv } = require('process');

let i = 0;
const noArg = 'No argument';
const arg = argv.splice(2);

while (arg[i] !== undefined) {
  i++;
}

if (i > 0) {
  console.log(arg[0]);
} else {
  console.log(noArg);
}
