// Form Handling of Request Submission


// Once someone click to submit of request form
$("#login").click(function()
{

	// Select the values from form Fields
	username=$("#user_name").val();
	password=$("#password").val();
	
	// Do the 
	$.ajax({

		type: "POST",
		url: "/submitrequestdata/",


		data: "billamount="+billamount+
			  "billidnumber="+billidnumber+
			  "&requesttype="+requesttype+
			  "&contact_num="+contact_num+
			  "&billing_company="+billing_company+
			  "&email_address="+email_address,


		// # .. On Success call
		success: function(response)
		{
			// # .. Print data to dev Console
			console.log(response)
		},


	});
	return false;
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





// beforeSend:function()
		// {
		// $("#add_err").html("Loading...")
		// }