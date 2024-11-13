module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
    'no-underscore-dangle': [
      'error',
      { 
        allow: [
          '_maxStudentsSize',
          '_amount',
          '_currency',
          '_name',
          '_length',
          '_students',
          '_code',
          '_sqft',
          '_floors',
          '_size',
          '_location',
          '_year',
          '_firstName',
          '_lastName',
          '_holbertonClass',
          '_brand',
          '_motor',
          '_color'
        ]
      }
    ],
  },
  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
