angular.module('app.routes', [])

  .config(function ($stateProvider, $urlRouterProvider) {

    // Ionic uses AngularUI Router which uses the concept of states
    // Learn more here: https://github.com/angular-ui/ui-router
    // Set up the various states which the app can be in.
    // Each state's controller can be found in controllers.js
    $stateProvider

    // **********************************************************
    // **                                                      **
    // **                       Student                        **
    // **                                                      **
    // **********************************************************


      .state('tabsController.profile', {
        url: '/studentProfile',
        views: {
          'tab1': {
            templateUrl: 'templates/Student/profile.html',
            controller: 'profileCtrl'
          }
        }
      })

      .state('tabsController.home', {
        url: '/studentHome',
        views: {
          'tab2': {
            templateUrl: 'templates/Student/home.html',
            controller: 'homeCtrl'
          }
        }
      })

      .state('tabsController.myJobs', {
        url: '/myJobsStudent',
        views: {
          'tab3': {
            templateUrl: 'templates/Student/myJobs.html',
            controller: 'searchCtrl'
          }
        }
      })

      .state('tabsController', {
        url: '/tab',
        templateUrl: 'templates/Student/tabsController.html',
        abstract: true
      })

      .state('tabsController.search', {
        url: '/searchStudent',
        views: {
          'tab2': {
            templateUrl: 'templates/Student/search.html',
            controller: 'searchCtrl'
          }
        }
      })

      .state('tabsController.search2', {
        url: '/searchPage',
        views: {
          'tab2': {
            templateUrl: 'templates/Student/search2.html',
            controller: 'search2Ctrl'
          }
        }
      })

      .state('tabsController.editProfile', {
        url: '/editProfile',
        views: {
          'tab1': {
            templateUrl: 'templates/Student/editProfile.html',
            controller: 'editProfileCtrl'
          }
        }
      })

      // **********************************************************
      // **                                                      **
      // **                 Business Sign Up                     **
      // **                                                      **
      // **********************************************************

      .state('businessTabsController.profile', {
        url: '/studentProfile',
        views: {
          'tab1': {
            templateUrl: 'templates/Business/profile.html',
            controller: 'businessProfileCtrl'
          }
        }
      })

      .state('businessTabsController.home', {
        url: '/studentHome',
        views: {
          'tab2': {
            templateUrl: 'templates/Business/home.html',
            controller: 'businessHomeCtrl'
          }
        }
      })

      .state('businessTabsController.search', {
        url: '/searchStudent',
        views: {
          'tab3': {
            templateUrl: 'templates/Business/search.html',
            controller: 'businessSearchCtrl'
          }
        }
      })

      .state('businessTabsController', {
        url: '/businessTab',
        templateUrl: 'templates/Business/tabsController.html',
        abstract: true
      })

      .state('businessTabsController.search2', {
        url: '/businessSearchPage',
        views: {
          'tab3': {
            templateUrl: 'templates/Business/search2.html',
            controller: 'businessSearch2Ctrl'
          }
        }
      })

      // **********************************************************
      // **                                                      **
      // **                 Login and Sign up                    **
      // **                                                      **
      // **********************************************************

      .state('login', {
        url: '/login',
        templateUrl: 'templates/login.html',
        controller: 'loginCtrl'
      })

      .state('signup', {
        url: '/signup',
        templateUrl: 'templates/signup.html',
        controller: 'signupCtrl'
      })

    $urlRouterProvider.otherwise('/login')


  });
