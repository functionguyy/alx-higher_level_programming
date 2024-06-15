#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

const n1 = parseInt(arg[0]);

function factorial (a) {
  if (a === 0) { return 1; } else { return (factorial(a - 1) * a); }
}

if (isNaN(n1)) {
  console.log(1);
} else {
  console.log(factorial(n1));
}
