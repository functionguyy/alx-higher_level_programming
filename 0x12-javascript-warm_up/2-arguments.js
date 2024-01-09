#!/usr/bin/node

const { argv } = require('process');

const argCount = argv.length - 2;
const noArg = 'No argument';
const oneArg = 'Argument found';
const moreArg = 'Arguments found';

if (argCount === 0) {
  console.log(noArg);
} else if (argCount === 1) {
  console.log(oneArg);
} else {
  console.log(moreArg);
}
