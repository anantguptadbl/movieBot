App.controller('movieController', ['$scope','$http','$compile', function($scope,$http,$compile) {
	// Main Javascript function that gets the search Results
	$scope.getSearchResults= function()
	{	
		$http({url:'/getMovies',method:"POST",params:{searchString:$scope.searchString}}).
				then(function successCallback(response) {
					//alert(response.data);
					$scope.searchResults=nouns=response.data['searchResults'];
					a=1;
				}, function errorCallback(response) {
					 }); 
		// End of the http call

	}// End of the function getSearchResults
}]);
    
