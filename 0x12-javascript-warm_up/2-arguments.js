#!/usr/bin/node

/* Check the number of arguments passed */
const numArgs = process.argv.length;

/* Print a message based on the numberof arguments */
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
