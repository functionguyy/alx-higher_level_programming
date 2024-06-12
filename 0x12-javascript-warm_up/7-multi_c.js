#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

const n1 = Number(arg[0]);

if (isNaN(n1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n1; i++) {
    console.log('C is fun');
  }
}
