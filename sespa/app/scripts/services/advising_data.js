'use strict';

/**
 * @ngdoc service
 * @name sespaApp.advisingService
 * @description
 * # advisingService
 * Factory in the sespaApp.
 */
angular.module('sespaApp')
  .factory('advisingData', function($http, $window) {
    var config = function() {
      return $http.get('api/', {
          'cache': true
        })
        .then(function(response) {
          if (response.data.username === '') {
            var current = $window.location.href;
            $window.location.href = response.data.login + '?next=' + current;
          }
          return response.data;
        });
    };

    var pushPaginatedData = function(obj, url) {
      $http.get(url).then(function(response) {
        response.data.results.forEach(function(entry) {
          obj.push(entry);
        });

        if (response.data.next !== null) {
          pushPaginatedData(obj, response.data.next);
        }
      });
    };

    // Public API here
    return {
      config: function() {
        return config();
      },

      allAdvisors: function() {
        return config().then(function(config) {
          return $http.get(config.advisors, {
              'cache': true
            })
            .then(function(response) {
              return response.data
            });
        });
      },

      advisorDetails: function(advisorName) {
        return config().then(function(config) {
          if (typeof advisorName === 'undefined') {
            advisorName = config.username;
          }
          return $http.get(config.advisors + advisorName + '/', {
              'cache': true
            })
            .then(function(response) {
              return response.data;
            });
        });
      },

      advisorsStudents: function(advisorName) {
        return config().then(function(config) {
          if (typeof advisorName === 'undefined') {
            advisorName = config.username;
          }
          return $http.get(config.advisors + advisorName + '/students/', {
              'cache': true
            })
            .then(function(response) {
              return response.data;
            });
        });
      },

      allStudents: function() {
        return config().then(function(config) {
          return $http.get(config.students, {
              'cache': true
            })
            .then(function(response) {
              return response.data
            });
        });
      },

      studentDetails: function(studentName) {
        return config().then(function(config) {
          return $http.get(config.students + studentName + '/full/', {
              'cache': true
            })
            .then(function(response) {
              return response.data;
            });
        });
      }

    };
  });
