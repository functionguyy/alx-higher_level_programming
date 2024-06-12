#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

const n1 = Number(arg[0]);

if (isNaN(n1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${n1}`);
}
