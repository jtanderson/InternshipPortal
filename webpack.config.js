const path = require("path");
const { VueLoaderPlugin } = require("vue-loader");
const Dotenv = require("dotenv-webpack");
const webpack = require("webpack");

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
    resolve: {
      extensions: [".tsx", ".ts", ".js", ".vue"],
      alias: {
        vue: "vue/dist/vue.esm-bundler.js",
      },
    },
    plugins: [
      new VueLoaderPlugin(),
      new Dotenv({ path: "./src/.env" }),
      new webpack.DefinePlugin({
        __VUE_OPTIONS_API__: false,
        __VUE_PROD_DEVTOOLS__: false,
      }),
    ],
  },
];
