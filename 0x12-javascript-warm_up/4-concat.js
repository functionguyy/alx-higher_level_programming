#!/usr/bin/node

const { argv } = require('node:process');

const args = argv.slice(2);
let result = '';
const str = ' is ';

result += args[0] + str + args[1];

console.log(result);
