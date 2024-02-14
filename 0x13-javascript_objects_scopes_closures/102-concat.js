#!/usr/bin/node

const fstr = require('fs');
const firstArg = fstr.readFileSync(process.argv[2]).toString();
const secondArg = fstr.readFileSync(process.argv[3]).toString();
fstr.writeFileSync(process.argv[4], firstArg + secondArg);
