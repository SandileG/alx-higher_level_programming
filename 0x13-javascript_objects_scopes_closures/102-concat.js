const fs = require('fs');

const filePath1 = process.argv[2];
const filePath2 = process.argv[3];
const destinationPath = process.argv[4];

fs.readFile(filePath1, 'utf8', (err, fileContent1) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.readFile(filePath2, 'utf8', (err, fileContent2) => {
    if (err) {
      console.error(err);
      return;
    }

    const combinedContent = fileContent1 + fileContent2;

    fs.writeFile(destinationPath, combinedContent, 'utf8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log('Files concatenated successfully!');
      }
    });
  });
});
