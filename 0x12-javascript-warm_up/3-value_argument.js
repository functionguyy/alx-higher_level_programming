#!/usr/bin/node

const { argv } = require('process');

let i = 0;
const noArg = 'No argument';
const lastItem = argv.at(-1);
i = argv.indexOf(lastItem);

if (i > 1) {
  console.log(argv[2]);
} else {
  console.log(noArg);
}
