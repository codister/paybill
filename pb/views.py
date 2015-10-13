from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pb.models import Merchent, Request, Payment, Company
from pb.forms import UserForm, MerchentForm
from django.shortcuts import render, get_object_or_404
from django.core import serializers

import json, time, requests


def index(request):
    # Just return the Landing page template back to the user!
    return render(request, "index.html")










# --- MERCHENT LOGIN --- #

def login_user(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:

            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied. Go back and try again")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'pb/login.html', {})

# --- MERCHENT REGISTERATION ---#
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of  UserForm 
        user_form = UserForm(data=request.POST)
        merchent_form = MerchentForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and merchent_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            merchent = merchent_form.save(commit=False)
            merchent.user = user

            # Did the user provide a merchent picture?
            # If so, we need to get it from the input form and put it in the merchent model.
            if 'cinc_selfi_photo' in request.FILES:
                merchent.cinc_selfi_photo = request.FILES['cinc_selfi_photo']
            if 'cnic_photo' in request.FILES:
                merchent.cnic_photo = request.FILES['cnic_photo']
            # Now we save the UserProfile model instance.
            merchent.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors and merchent_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        merchent_form = MerchentForm()

    # Render the template depending on the context.
    return render(request,
            'pb/register.html',
            {'user_form': user_form, 'registered': registered, 'merchent_form': merchent_form} )

# Getting the User Logged out of the System
@login_required
def user_logout(request):

    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


# --- DASHBOARD --- #

# .. Get the Current logged in user
# .. Get the Claimed Request which needs to be process by current logged in users
# .. Get the Pending Request which need to be process and also exclude where isCLaimed attribute is True
# .. Add Pagination for Bulk Records
# .. 

# --- Claim a Request --- #

# .. Get the id of request to be claimed
# .. Get the Current USER
# .. Get a single request record by id
# .. Change the Attribute value (isClaimed) to True of Request Record we just got from database
# .. Log the current time in claimed on timming attribute of request
# .. 

# --- Time Remaing to Process a Request Calculator --- #

# .. Make sure if current is has claimed the request he is trying to get the time for (Optional)
# .. Get the Current time
# .. Get the time when request was claimed on
# .. get the time difference
# .. GEt the Attribute time remaing and store it in there
# .. Get the claim on timming Attribute value of request we are trying to calculate time for
# .. Calculate the x time passed away since the request is claimed
# .. If the x time is more then 30 mints then change the transaction isClamed attribute status to false
# .. If the x time is less then 30 mints then return remaining time to complete the transaction to current time


# --- PAYMENTS --- #

# .. Get the payments history
# .. Request Payment create payment object
# .. Get the payment by pk

# --- Track Transfers --- #

# --- Requests --- #

# .. Get the request detail by request id
def get_request(request, request_id):
    # .. Get the record by request ID
    req = get_object_or_404(Request, pk=request_id)
    
    # .. Get the Status of request
    if req.is_completed:

        jsonrecord = json.dump(req)
        
        # .. Code it to Json and return
        return HttpResponse(jsonrecord)


# .. # .. /claim-request/<request_id>
# .. Claim a request to process by passing the req id
# .. Make sure if the request_token is set to false 
# .. check if user is activated and approved
# .. add or update the request claimed time field in database
# .. update the time remaining to process a request set call the calculate functions
# .. redirect to confim request completed page /request_confirm/<request_id>



# .. /request_confirm/<request_id>
# .. Mark the request completed by providing the confirmation number
# .. Check if the ID Confirmation is provided
# .. check if the request if claimed by logged in user
# .. check if the request has a request token True # if not then tell user time expired to process this request claim it again from claiming section to process it again
# .. if this all sounds great means true then we go ahead
# .. mark the request completed in DB field and notify the user by email




# .. /requests-completed/
# .. Request completed by logged in user
# .. Get the logged in user by request object
# .. Query the ORM by saying select from model request where user id is user logged in
# .. Return the request completed by logged in to template called completed request


# .. /requests-claimed/
# .. Return the the request claimed and not yet completed of logged in merchent user
# .. Get the logged in user
# .. query the orm where user id is logged in user and request are claimed by current logged in user 
# .. and are still pending and have request token True so that they know they can still process it



# .. /time-lef/<request_id> = AJAX expects a request id to get it's time left
# .. Trigger this function every 30 mints to check time remaining to process request
# .. if time is not greater then 30 mints from the time request claim then do nothing
# .. else if time is greater then 30 mints from the time request was claim then expire
# .. the token by changing the db field called request_token to False so



# .. /search_request/<search_text>/
# .. Get the request by their bill type
# .. Search within bill types, companies, request id, email address, request phone
# .. return the object got to template and render it no results found on template end by using count tag/filter




def submit_request_data(request):
    ## Data Validations Needed for Security
    # .. Validate Country Later (())... 
    # .. Validate whether or not given company supports such service that user gave us
    # .. validate if support such company
    # .. Validate if we support such service

    if request.method == 'POST':

        billamount  = request.POST.get('billamount')
        requesttype = request.POST.get('requesttype')
        country     = request.POST.get('country')
        contact_num = request.POST.get('contact_num')
        billing_company = request.POST.get('billing_company')
        email_address = request.POST.get('email_address')

        # Generate the bitfinex address and return to the user
        newly_generated_address = gen_deposit_address()
        
        # Convert from PKR to BTC on the fly!
        btc_amount_to_paid = exhange_pkr_to_btc(billamount)
        
        # Save the details to database
        yoorequest = Request.create( 
            
            pkr_bill_amount=billamount, 
            requesttype=requesttype, 
            country=country, 
            contact_num=contact_num, 
            billing_company=billing_company, 
            email_address=email_address, 
            btc_address=newly_generated_address,
            btc_amount=btc_amount_to_paid

            )

        # Encode the DICT to Json
        response = {

            "amountdue" : btc_amount_to_paid,
            "baddress"  : newly_generated_address

        }

        # Return a message that data has been saved in Json Format
        return HttpResponse(json.dumps(response))
    else:
        # Do a redirect we don't have Post Request Comming!
        return HttpResponseRedirect("/404")


# # --- View for check how much confirmation have been made in there --- #
# def is_request_paid(request, request_id):
#     # .. Call the function btc_tranx_detail
#     # .. Access the balance on this address 
#     # .. if address have balance > 0 and is = to ammount to bill to be paid
#     # ... Mark the item as paid in DB field so we can keep track of it
#     # ... Return payment has been made in Json
#     # .. else we did not got the payment return error message with no payment made yet
#     # ... returm error no payment made yet (json)



# # --- We want to make sure if we the request have 
# def is_payment_completed(request, request_id):
#     # Call the function btc_tranx_detail which returning DICT
#     # Get the BTC address from Request model with request ID
#     # check if payment_completed is not set to true
#     # Access the confirmations field value with BTC address
#     # now we need to check the confirmations
#     # Get the confirmations if it's great then 6 then we marke it full safe
#     # Mark the item payment_completed to true in DB field & return good message
#     # if it's not else return error message not yet completed




def get_companies(request, bill_type):

    companies = Company.objects.all().filter(bill_type=bill_type)
    data = serializers.serialize("json", companies)
    return HttpResponse (data)






############################
# --- Helper Functions --- #
############################


def exhange_pkr_to_btc(amount):
    # First of all get the exhange rate
    
    # Make a get request to https://api.blinktrade.com/api/v1/PKR/ticker
    data = requests.get("https://api.blinktrade.com/api/v1/PKR/ticker").json()
    
    # Access and store the variable ( exchange rate )
    pkr_exhange_rate = data["buy"]
    
    # Convert the PKR amount to BTC
    return amount / pkr_exhange_rate





# --- Get the BTC TRANSACTION details with BTC address --- #
def btc_tranx_detail(btc_address):
    # http://api.blockcypher.com/v1/btc/main/addrs/3HcGoxru2msKRcmpktDNSrAgNCB9B7Zu4V
    # Make a get request to the URL with Dynamic Address
    trx_details = requests.get( "http://api.blockcypher.com/v1/btc/main/addrs/" + btc_address ).json()
    
    # return the DICT
    return trx_details





# --- Generate a new address for making payments from bitfinex --- #
def gen_deposit_address():
    # Import specific to this function
    import base64
    import hashlib
    import hmac

    # Main Function begins
    bitfinexURL = 'https://api.bitfinex.com/v1/deposit/new'
    bitfinexKey = 'J4HZgO4DWeKDV9el4NcGcuHPRsOXzOSpGhczVyzpBSM'
    bitfinexSecret = b'C9Jl818rNbUUzoOKAsoEYIBUdy8kBQLM0uRmZLAP1zL' #the b is deliberate, encodes to bytes

    payloadObject = {
            'request':'/v1/deposit/new',
            'nonce':str(time.time() * 100000), #convert to string
            'method':'bitcoin',
            'wallet_name':'deposit',
            'renew':1
    }
    # Preparing the payload data
    payload_json = json.dumps(payloadObject)
    payload = base64.b64encode(bytes(payload_json, "utf-8"))

    m = hmac.new(bitfinexSecret, payload, hashlib.sha384)
    m = m.hexdigest()

    #headers
    headers = {
          'X-BFX-APIKEY' : bitfinexKey,
          'X-BFX-PAYLOAD' : base64.b64encode(bytes(payload_json, "utf-8")),
          'X-BFX-SIGNATURE' : m
    }

    r = requests.get(bitfinexURL, data={}, headers=headers)
    bit_data = r.json()
    return bit_data['address']['address']