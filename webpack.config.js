var path = require('path');

module.exports = {
  //entry: "./app/static/js/index.entry.js",
  entry: {
    'index': './app/static/js/index.entry.js',
    'admin': './app/static/js/event.entry.js'
  },
  output: {
    path: __dirname,
    filename: './app/static/assets/[name].js'
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