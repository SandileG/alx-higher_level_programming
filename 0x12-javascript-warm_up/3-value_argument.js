#!/usr/bin/node

/* Check if an argument is passed */
const arg = process.argv[2];

/* Print the argument or "No argument" if no argmument is passed */
console.log(arg || 'No argument');
