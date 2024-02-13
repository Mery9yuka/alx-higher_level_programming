#!/usr/bin/node

const s = parseInt(process.argv[2]);

if (!isNaN(s)) {
  for (let j = 0; j < s; j++) {
    console.log('X'.repeat(s));
  }
} else {
  console.log('Missing size');
}
