

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


	$("#loading-ajax").show();

// Hide the form fields, previous, and submit button
	$("#removefinal").hide()
	$("#previous-step").remove();
	$("#next-step").remove();
	$("#button-control").empty();

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

			
			// show the payment detail div so we print our
			// .. Server generated details and append into it
			$("#loading-ajax").hide();
			$("#show_payment_details").show();

			// Show the user Request id along with btc addressa , 
			// amount due and time left to complete the purchase

			$("#btc-address").append(btc_address);
			$("#due-amount").append(amount_due);
			$("#request-id").append(request_id);
			// Storing it hidden on page
			$("#hidden-request-id").append(request_id);

			//Show the button to check if the payment is completed
			$("#outer-form").append("<div id='payment-confirm-div' class='text-center'><button id='payment-check' class='wizard-finish btn btn-success' type='submit'><i class='fa fa-check-circle-o fa-spin'></i> Check Payment</button></div></br>");

		},

		complete : function() {
			$("#payment-check").click(function(){

				var request_id = $("#hidden-request-id").text();
				$("#loading-ajax").show();
				$("#show_payment_details").hide();


				$.ajax({

					type: "GET",
					url: "/isrequestpaid/" + request_id + "/" ,

					// very important or you'll get string stripped
					dataType: "json",

					// # .. On Success call
					success: function(data) {

						// # .. Print data to dev Console
						console.log(data);
						ispaid = data["ispaid"];
						minleft = data["leftmin"];

						console.log(ispaid);
						console.log(minleft);


						if (ispaid == "true" && minleft !== "0") {

							$("#loading-ajax").hide();
							$("#payment-confirm-div").hide();
							$("#confirm-payment").show();
							console.log("i'm being excuted after the success div")

						};

						if (ispaid == "false") {
							//show error message we got most likley i would turn this into a function
							$("#loading-ajax").hide();
							$("#show_payment_details").show();

							$("#jumping-jack").show();
						};

					}, // end of suceesfull call excution function
				}); // end of ajax call
			   
			});
		},

	});
	
});




// AJAX form handling for submit request 
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



// Workaround to hide a default div to and 
// .. to show it on demand based on ajax request
// .. We are going to hide some div's as soon as page loads
$(document).ready(function() 
{
    $("#jumping-jack").hide();
    $("#show_payment_details").hide();
	$("#loading-ajax").hide();
	$("#confirm-payment").hide();

});
