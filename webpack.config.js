const path = require('path');

module.exports = {
  entry: './myapp/static/main.js',  // Replace with the path to your main JavaScript file
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static2/js'),  // Replace with the desired output directory
  },
};