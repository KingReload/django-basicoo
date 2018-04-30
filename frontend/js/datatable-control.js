$(document).ready(function($) {
	$('#table-control').DataTable( {
		"pagingType": "full_numbers",  
    	"iDisplayLength": 13,
		"bFilter" : false,
		"bLengthChange": false,
    	"bSort": false
    });
});
