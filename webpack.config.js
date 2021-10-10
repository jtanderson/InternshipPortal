const path = require("path");
const { VueLoaderPlugin } = require("vue-loader");
const Dotenv = require("dotenv-webpack");

module.exports = [
  {
    mode: "development",
    entry: "./src/main.js",
    output: {
      path: path.resolve(__dirname, "static/dist"),
      filename: "bundle.js",
    },
    resolve: {
      alias: {
        vue: "vue/dist/vue",
        css: "tailwindcss/dist/tailwindcss",
      },
    },
    module: {
      rules: [
        {
          test: /\.vue/,
          loader: "vue-loader",
        },
        {
          test: /\.css$/i,
          use: ["style-loader", "css-loader", "postcss-loader"],
        },
        {
          test: /\.(png|svg|jpg|jpeg|gif)$/i,
          type: "asset/resource",
        },
      ],
    },
    plugins: [new VueLoaderPlugin(), new Dotenv({ path: "./src/.env" })],
  },
];
