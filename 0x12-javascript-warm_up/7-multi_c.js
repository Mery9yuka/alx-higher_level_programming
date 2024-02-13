#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!isNaN(x)) {
    for (let j = 0; j < x; j++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
