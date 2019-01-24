App.config(function($routeProvider) {
  $routeProvider
	.when('/', {
	templateUrl: 'static/views/about.html',
	controller: 'aboutController'
	})
	.when('/about', {
	templateUrl: 'static/views/about.html',
	controller: 'aboutController'
	})
	.when('/movie', {
	templateUrl: 'static/views/movie.html',
	controller: 'movieController'
	})
	.when('/contact', {
	templateUrl: 'static/views/contact.html',
	controller: 'contactController'
	})
        .otherwise({
        redirectTo: '/404'
    });
});
