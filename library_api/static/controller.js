var app = angular.module('firstApp', []);
app.controller('ctrl', function($scope,$http) {
	$http({
		method: 'GET',
		url: 'http://127.0.0.1:8000/books/'
		 }).then(function (response){
			 $scope.userslist=response.data;
		 },function (error){
			 $scope.userslist=["Error in connection"];
	});
	$scope.myFunction = function() {
		var url = 'http://127.0.0.1:8000/books/';
		var data=
			{
				"isbn": $scope.isbn,
				"book_name": $scope.book_name,
				"author": $scope.author,
				"no_of_actual_copies":$scope.ac_copy,
				"no_of_cuurent_copies":$scope.cu_copy
			};
		var headers= {'Content-Type': 'application/json'};
    	$http.post(url, data,headers).then(function (response) {
			$http({
				method: 'GET',
				url: 'http://127.0.0.1:8000/books/'
				 }).then(function (response){
					 $scope.userslist=response.data;
				 },function (error){
					 $scope.userslist=["Error in connection"];
			});
		});
	};
});