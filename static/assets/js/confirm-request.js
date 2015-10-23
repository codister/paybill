$(document).ready(function(){
     intervalid = setInterval(get_time_left(), 1000);
     console.log(intervalid);
 });

 function get_time_left(){

 	var request_id = $("#request-id").text();

     $.ajax({
         url: '/mercehenttimeleft/' + request_id + '/',
         dataType : "json",

         success: function(data) {
         	console.log(data)
	         minleft = data["minleft"];
	         secleft = data["secleft"];
	         console.log(minleft);
	         console.log(secleft);

	         console.log("the interval id is : ", intervalid);

	         if (minleft == "0") {

	         	// clear the interval if possible
	         	clearInterval(intervalid);

	         };

	         minsec  = minleft + ":" + secleft; 
             $('#minsec').html(minsec);
         }
     });
 }