#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    const concatenatedData = dataA + '\n' + dataB;
    fs.writeFile(destinationPath, concatenatedData, err => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Files ${fileAPath} and ${fileBPath} concatenated and saved to ${destinationPath}`);
    });
  });
});
