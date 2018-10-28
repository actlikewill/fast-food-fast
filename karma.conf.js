module.exports = function (config) {
  config.set({
    frameworks: ['jasmine', 'jasmine-matchers'],
    preprocessors: {
      '*.js': ['coverage']
    },
    files: [
      "./custom-matchers.js",
      '*.js',
      '*.spec.js'
    ],
    plugins: [
      'karma-jasmine',
      'karma-jasmine-matchers',
      'karma-chrome-launcher',
      'karma-coverage',
      'karma-coveralls'
    ],
    reporters: ['dots', 'coverage', 'coveralls'],
    colors: true,
    browsers: ['ChromeHeadless'],
    singleRun: true,
    coverageReporter: {
      dir: 'coverage/',
      type: 'lcov'
      
    }
  })
};
