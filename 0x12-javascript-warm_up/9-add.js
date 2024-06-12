#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

function add (a, b) {
  const result = parseFloat(a) + parseFloat(b);
  console.log(result);
}

add(arg[0], arg[1]);
