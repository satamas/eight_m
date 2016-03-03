var path = require('path');

module.exports = {
  entry: "./app/static/js/index.entry.js",
  output: {
    path: __dirname,
    filename: "./app/static/assets/index.js"
  },
  module: {
    loaders: [
      {
        test: /\.css$/,
        loader: "style!css"
      }
    ]
  }
};