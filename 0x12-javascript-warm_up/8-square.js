#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

const n1 = Number(arg[0]);
let result = '';
const str = 'X';

if (isNaN(n1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n1; i++) {
    for (let j = 0; j < n1; j++) {
      result += str;
    }
    console.log(result);
    result = '';
  }
}
