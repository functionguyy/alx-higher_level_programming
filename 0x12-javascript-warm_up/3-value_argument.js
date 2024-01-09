#!/usr/bin/node

const { argv } = require('process');

let i = 0;
const noArg = 'No argument';
for (const name of argv){
  i++;
}

if (i > 2){
  console.log(argv[2]);
} else {
  console.log(noArg);
}
