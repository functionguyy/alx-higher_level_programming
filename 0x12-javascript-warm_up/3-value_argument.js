#!/usr/bin/node

const { argv } = require('process');

let i = 0;
const noArg = 'No argument';
for (const name of argv.slice(2)){
  i++;
}

if (i > 0) {
  console.log(argv[2]);
} else {
  console.log(noArg);
}
