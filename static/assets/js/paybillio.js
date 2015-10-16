// Form Handling of Request Submission


// Once someone click to submit of request form
$("#submit_req_form").click(function()
{

	// Select the values from form Fields
	bill_type=$("#validation-bill_type").val();
	billing_company=$("#validation-billing_company").val();
	email_address=$("#validation-email").val();
	date=$("#validation-date").val();
	billidnumber=$("#validation-billidnumber").val();
	billamount=$("#validation-billamount").val();
	contact_num=$("#validation-contact_num").val();
	
	// Do the 
	$.ajax({

		type: "POST",
		url: "/submitrequestdata/",
		dataType : "json",

		data:  {
					"billamount"     	: billamount,
				  	"billidnumber"  	: billidnumber,
				  	"bill_type"    		: bill_type,
				  	"contact_num"  		: contact_num,
				  	"billing_company" 	: billing_company,
				  	"email_address"	    : email_address
			   },


		// # .. On Success call
		success: function(response) {
			// # .. Print data to dev Console
			var data = response;

			btc_address = data["baddress"];
			amount_due  = data["amountdue"];
			request_id  = data["requestid"];

			console.log(response);

			console.log("Response from the server OK 200");
			console.log(btc_address);
			console.log(amount_due);
			console.log(request_id);


			// Hide the form fields, previous, and submit button
			$("#removefinal").hide()
			$("#previous-step").remove();
			$("#next-step").remove();
			$("#button-control").empty();

			//Show the button to check if the payment is completed
			$("#button-control").append("<button id='payment-check' class='wizard-finish btn btn-success' type='submit'><i class='fa fa-check-circle-o fa-spin'></i> Check Payment</button>");
			
			// show the payment detail div so we print our
			// .. Server generated details and append into it
			$("#show_payment_details").show();

			// Show the user Request id along with btc addressa and amount due in BTC

		},

	});
	
	return false;
});



// Once user click to confirm the payment we check and tell him if it happend or not
// .. if it does then make a request call to confim payment URL
// .. If not then tell user we did not recived the funds or he belives it's an error
// .. then he should be sending us email along with request ID he gotå

$("#payment-check").click(function()
{


	$("#show_payment_details").hide();
	$("#loading_ajax").show();

	$.ajax ({

		type: "GET",
		url: "/isrequestpaid/" + request_id + "/" ,

		// very important or you'll get string stripped
		dataType: "json",

		// # .. On Success call
		success: function(data) {

			console.log("i m success call function which excutes after user clicks payment check button")
			console.log(data)

			var ispaid = data["ispaid"]
			var request_id = ["requestid"]
			var is_time_left = data["istimeleft"]

			if ( ispaid == true && istimeleft == true ) {

				// ok then now we now we got the payment tell the user and user have
				// .. paid the payment within given period of time

				// ... Hide the payment info div
				
				// ... Show the div with big success message and tverse values to screen



			}else{

				// Error notification handling

				// show the error message tell the error message to user

				if ( ispaid == true && is_time_left == false ) {


					// Issue a error message saying we got a payment 
					// But you were to late to complete the payment within given time period

					$("#show_payment_details").show();

				};

				if ( ispaid == false && is_time_left == true ) {

					// Issue error message no payment got at all
					// but you can still try again to pay you have time left to pay your
					// request

					$("#show_payment_details").show();

				};


				if ( ispaid == false && is_time_left == false ) {


					// No payment got niether user have time left to pay a it
					// so restart the request process

					console.log("No Payment or anything restart the Request process");


				};
			};



		}, // end of suceesfull call excution function

	}); // end of ajax call 


});








///////										  	 //////
//////  AJAX form handling for submit request  ///////
/////										 ////////


$('#validation-bill_type').on('change', function() {
	
	var bill_type = $(this).val();

	$.ajax({

		type: "GET",
		url: "/getcompanies/" + bill_type + "/" ,

		// very important or you'll get string stripped
		dataType: "json",

		// # .. On Success call
		success: function(data) {

			// # .. Print data to dev Console
			var items = data

			// Remove the default work 
			$("#validation-billing_company option[value='None']").remove();

			// Animate the field so user knows they got new
			$("#billing_company").addClass("animated bounce");

			// Loop over the data we got from ajax call
			for ( var i = 0; i < items.length; i++ ) 
			{
				
				// add the option to existing select options
				$('#validation-billing_company').append($('<option>', { 
			        
			        // Extracting and appending values
			        value: items[i]["pk"],
			        text : items[i]["fields"]["name"]
			    
			    })); // end appending options from data we got from server 
			}; // end of for loop of response 
		}, // end of suceesfull call excution function
	}); // end of ajax call 
}); // ending the change state option









				
////////////
///////////		MANIPULATIING THE DOM 


// Workaround to hide a default div to and 
//to show it on demand based on ajax request

$("#next-step").click(function()
{
	
	$("#show_payment_details").hide();
	$("#loading_ajax").hide();

});