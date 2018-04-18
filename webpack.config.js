'use strict'

const CopyWebpackPlugin = require('copy-webpack-plugin')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const ImageminPlugin = require('imagemin-webpack-plugin').default
// const UglifyJSPlugin = require('uglifyjs-webpack-plugin')
const autoprefixer = require('autoprefixer')
const path = require('path')
const webpack = require('webpack')

module.exports = [
  {
    entry: {
      'bootstrap/bootstrap': './frontend/js/bootstrap/bootstrap.js',
      main: './frontend/js/myscript.js',
    },
    output: {
      filename: '[name].js',
      path: path.resolve(__dirname, 'basicoo/static/js'),
      publicPath: '/static/',
      sourceMapFilename: 'sourcemaps/[name].map'
    },
    module: {
      rules: [{
        test: /\.(css|scss)$/,
        loader: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
              {
                loader: "css-loader",
                options: {
                  sourceMap: true,
                }
              },
              {
                loader: "postcss-loader",
                options: {
                  sourceMap: true,
                  plugins: [
                      autoprefixer
                  ]
                }
              },
              {
                loader: "sass-loader?sourceMap",
                options: {
                  includePaths: [
                    './frontend/css'
                  ]
                }
              },
            ]
        })
      }, {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader'
        }
      }, {
        test: /\.(png|jpg|jpeg|gif)/,
        loader: 'file-loader',
        options: {
          name: '[path][name].[ext]',
          context: 'frontend/images',
          outputPath: 'images/',
          publicPath: '/static/'
        }
      }]
    },
    resolve: {
      alias: {
        jquery: "jquery/jquery-3.2.1.js"
      },
      modules: [
        path.resolve(__dirname, 'node_modules'),
        path.resolve(__dirname, 'frontend'),
        path.resolve(__dirname, 'frontend', 'images'),
        path.resolve(__dirname, 'frontend', 'css'),
        path.resolve(__dirname, 'frontend', 'js'),
      ]
    },
    plugins: [
      new webpack.ProvidePlugin({
          $: "jquery",
          jQuery: "jquery"
      }),
      new CopyWebpackPlugin([
        { from: 'frontend/css/', to: '../css' },
        { from: 'frontend/images/', to: '../images' }
      ]),
      new ExtractTextPlugin({
        filename: '[name].css',
        allChunks: true
      })
    ]
  },
]