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
			  "&requesttype="+requesttype+
			  "&country="+country+
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


// beforeSend:function()
		// {
		// $("#add_err").html("Loading...")
		// }