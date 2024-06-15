#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.slice(2);

let n;
let p;

if (arg.length === 0 || arg.length === 1) {
  p = 0;
} else {
  for (let i = 0; arg[i] !== undefined; i++) {
    const num = Number(arg[i]);
    if (i === 0) {
      n = num;
      p = 0;
    }
    if (i !== 0) {
      if (num > n) {
        p = n;
        n = num;
      }
      if (num < n && num > p) {
        p = num;
      }
    }
  }
}

console.log(p);
