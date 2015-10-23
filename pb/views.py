from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pb.models import Merchent, Request, Payment, Company
from pb.forms import UserForm, MerchentForm
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime, timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Standard Import related to Python
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


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    print("user was logged in and we logged him out")
    logout(request)
    
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

# --- Requests --- #

#####################################################
####                                             ####
####  Merchent Area Requests view and Processing ####
####                                             ####
#####################################################

# --- Requests --- #

# .. # .. /claim-request/<request_id>
# .. Claim a request to process by passing the req id
def claim_request(request, request_id):
    # get the object
    bill_request = Request.objects.get(pk=request_id)
    # .. Make sure if the request_token is set to false 
    if bill_request.request_token == True:
    # .. add or update the request claimed time field in database
        bill_request.time_claimed_on = datetime.now(timezone.utc)
        logged_in_merchent = Merchent.objects.get(user_id=request.user.pk)
        bill_request.claimer = logged_in_merchent
        bill_request.request_token = False
        bill_request.save()
        # .. redirect to confim request completed page /request_confirm/<request_id>
        redirect_url = "/confirm-request/" + str(bill_request.pk)
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse("not available for claim")


# .. /confirm-request/<request_id>
# .. Mark the request completed by providing the confirmation number
def confirm_request(request, request_id):
    # check if we got the form submitted or get request
    if request.method == 'POST':
        txid = request.POST.get('txid')
        # Validate this string before putting it in the database
        ## todo
        # get the object by id
        bill_request = Request.objects.get(pk=request_id)
        # save it in database
        bill_request.confirmation_txid = txid
        bill_request.is_completed = True
        # save it in DB
        bill_request.save()
        # render the form
        # send email todo
        context = {
            
            "request" : bill_request,
            "messagetype" : "success"
        }
        return render(request, 'pb/confirm_request.html', context )
    else:
        # display the request information

        bill_request = Request.objects.get(pk=request_id)

        print("Request Status is : ", bill_request.is_completed  )

        # get the request information
        context = {

            "request" : bill_request
        
        }
        return render(request, 'pb/confirm_request.html', context )



# Pool of Bill Request shown all Merchents so they can process requests
def bill_requests(request):
    # get all the objects with respect to unclaimed and have token to setten to false
    bill_requests_list = Request.objects.all().filter(request_token=True, is_completed=False)

    paginator = Paginator(bill_requests_list, 10) # Show 10 bills per page

    page = request.GET.get('page')
    try:
        bill_requests = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bill_requests = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bill_requests = paginator.page(paginator.num_pages)

    context = {

        "bill_requests" : bill_requests 

    }

    return render(request, "pb/latest_requests.html", context)


# Claimed Un Processed Requests
def merchent_claimed_requests(request):
    bill_requests = Request.objects.all().filter(claimer_id=request.user.pk, is_completed=False)

    context = {

        "bill_requests" : bill_requests

    }

    return render(request, "pb/claimed_requests.html", context)
    


# Completed Requests by Logged in Merchent User
def merchent_completed_requests(request):
    bill_requests = Request.objects.all().filter(claimer_id=request.user.pk, is_completed=True)

    context = {

        "bill_requests" : bill_requests

    }
    
    return render(request, "pb/completed_requests.html", context)



# --- DASHBOARD --- #
def merchent_dashboard(request):
    bill_requests = Request.objects.all().filter(request_token=True, is_completed=False)
    completed_requests = Request.objects.all().filter(claimer_id=request.user.pk, is_completed=True)
    logged_in_merchent = Merchent.objects.get(pk=request.user.pk)

    # GET payments for logged in merchent

    payments = Payment.objects.all().filter(merchent_id=logged_in_merchent.pk)

    context = {

        "bill_requests" : bill_requests,
        "completed_requests" : completed_requests,
        "payments" : payments,
        "merchent" : logged_in_merchent

    }
    
    return render(request, "pb/merchent_dashboard.html", context)


# --- PAYMENTS --- #

# .. Get the payments history
def all_merchent_payments(request):
    return HttpResponse("Return Payments here")

# .. Request Payment create payment object

def create_payment(request):
    if request.method == 'POST':
        # get the data from post request like payment amount request , and payment method
        raw_amount_requested = request.POST.get('requestamount')
        payment_method  = request.POST.get('paymentmethod')
        amount_requested = int(raw_amount_requested)
        #Todo Validated the Post data from injections etc clean it off

        # Available Balance
        logged_in_merchent = Merchent.objects.get(user_id=request.user.pk)

        if amount_requested < logged_in_merchent.balance_available:
            # ok go ahead user have requested from available
            # Create a Payment request
            payment = Payment.objects.create(
                payment_amount = amount_requested,
                payment_method= payment_method,
                merchent=logged_in_merchent

                )
            # - the request amount from available balance
            logged_in_merchent.balance_available = logged_in_merchent.balance_available - amount_requested
            # save the changes to merchent model
            logged_in_merchent.save()

            # Debug 
            print(payment)

            #return the response
            context = {

                "error" : "false",
                "payment_id" : payment.pk,
                "payment_amount" : payment.payment_amount
            }

            #debug
            print(context)

            return HttpResponseRedirect("/payments")
        else:
            return HttpResponseRedirect("/")

# .. Get the payment by pk

def payment(request, request_id):
    return HttpResponse(request_id)



def all_payments(request):

    payments = Payment.objects.all()
    logged_in_merchent = Merchent.objects.get(user_id=request.user.pk)

    context = {

        "payments" : payments,
        "merchent" : logged_in_merchent 

    }

    return render(request, "pb/all_payments.html", context)
# --- Track Transfers --- #


#######################################
####                               ####
####  Merchent's API Interactions  ####
####                               ####
#######################################


def merchent_time_left(request, request_id):
    # Get the Bill request of which we need time remaining
    bill_request = Request.objects.get(pk=request_id)
    # Get the time right now server time
    time_now = datetime.now(timezone.utc).replace(microsecond=0)
    print(time_now)

    # Get the time difference
    request_claimed_time = bill_request.time_claimed_on.replace(microsecond=0)
    print(request_claimed_time)
    
    # TimeDelta class base time difference between two results
    time_difference = time_now - request_claimed_time 

    # print the time right now in UTC

    # print the time of request initiated
    print("Time difference is : " , time_difference)

    # Get the time difference in Minutes for more readable format
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Check if time ago is less in [30] minutes
    if minutes < 30 :
        timeleft_min = 30 - minutes
        timeleft_sec = seconds
    else:
        timeleft_min = 0
        bill_request.token = True
        bill.request.claimer = Merchent.objects.get(pk=1)
        bill_request.save()
        timeleft_sec = seconds


    response = {

        "minleft" : timeleft_min, 
        "secleft" : timeleft_sec
    }

    # Return Json encoded response 
    return HttpResponse(json.dumps(response))


#####################################################
####                                             ####
####  Front end User Request's API Interactions  ####
####                                             ####
#####################################################


@csrf_exempt
def submit_request_data(request):
    ## Data Validations Needed for Security
    # .. Validate Country Later (())... 
    # .. Validate whether or not given company supports such service that user gave us
    # .. validate if support such company
    # .. Validate if we support such service

    if request.method == 'POST':

        billamount  = request.POST.get('billamount')
        bill_type = request.POST.get('bill_type')
        country     = request.POST.get('country')
        contact_num = request.POST.get('contact_num')
        billing_company = request.POST.get('billing_company')
        email_address = request.POST.get('email_address')
        billidnumber = request.POST.get('billidnumber')

        # Generate the bitfinex address and return to the user
        newly_generated_address = gen_deposit_address()
        
        # Convert from PKR to BTC on the fly!
        bill_in_int = int(billamount)
        btc_amount_rep = exhange_pkr_to_btc(bill_in_int)
        
        # limit the btc amount amount to be paid to show 8 digits after decimal points
        limited_str = '%.8f' % (btc_amount_rep)
        # convert it back to flaot in to same variable
        btc_amount_to_paid = float(limited_str)
        # Default user which is Admin it self
        default_merchent = Merchent.objects.all().filter(pk=1)
        # Save the details to database
        yoorequest = Request.objects.create( 
            
            pkr_bill_amount=billamount, 
            bill_type=bill_type,
            contact_num=contact_num, 
            billing_company=billing_company, 
            bill_id_num=billidnumber,
            email_address=email_address, 
            btc_address=newly_generated_address,
            btc_amount=btc_amount_to_paid,
            time_claimed_on=datetime.now(timezone.utc),

            )

        # Debug

        print (yoorequest)
        print (yoorequest.pk)

        # Encode the DICT to Json
        response = {
            "requestid" : yoorequest.pk,
            "amountdue" : btc_amount_to_paid,
            "baddress"  : newly_generated_address,
            "status"    : "true"

        }

        print(response)

        # Return a message that data has been saved in Json Format
        return HttpResponse(json.dumps(response))
    else:
        # Do a redirect we don't have Post Request Comming!
        return HttpResponseRedirect("/404")


# --- View for check how much confirmation have been made in there --- #
def is_request_paid(request, request_id):
    # .. Get the BTC address by request ID
    bill_request = Request.objects.get(pk=request_id)
    # .. Call the function btc_tranx_detail
    trx_details = btc_tranx_detail(bill_request.btc_address)

    # Get the time right now server time
    time_now = datetime.now(timezone.utc).replace(microsecond=0)
    print(time_now)

    # Get the time difference
    request_creation_time = bill_request.date_time.replace(microsecond=0)
    print(request_creation_time)
    
    # TimeDelta class base time difference between two results
    time_difference = time_now - request_creation_time 

    print(time_difference)

    # Get the time difference in Minutes for more readable format
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Check if time ago is less in [30] minutes
    if minutes < 30 :
        timeleft_min = 30 - minutes
        timeleft_sec = seconds
    else:
        timeleft_min = 0
        timeleft_sec = seconds

    print(timeleft_min)

    
    # .. Debug mode
    # print (trx_details)
    # print (type(trx_details))

    # .. Access the balance on this address and convert from Satoshi to BTC
    balance_receive = trx_details["total_received"] / 100000000

    print (bill_request.btc_amount)
    print ("Balance Received from User", balance_receive)

    # .. if address have balance > 0 and is = to ammount to bill to be paid
    if balance_receive == bill_request.btc_amount:
        # ... Mark the item as paid in DB field so we can keep track of it
        bill_request.ispaid = True
        bill_request.save()
        # ... Return payment has been made in Json
        response = {
            "ispaid"     : "true",
            "requestid"  : request_id,
            "leftmin"    : timeleft_min,
            "leftsec"    : timeleft_sec
        }
    # .. else we did not got the payment return error message with no payment made yet
    else:
        response = {
            # change "ispaid" to false" debug only
            "ispaid"     : "true",
            "requestid"  : request_id,
            "leftmin"    : timeleft_min,
            "leftsec"    : timeleft_sec
        }

    # .. returm error no payment made yet (json)
    return HttpResponse(json.dumps(response))


# --- time in minuted left to pay bill request --- #
def time_left_to_pay(request, request_id):
    # Get the Bill request of which we need time remaining
    bill_request = Request.objects.get(pk=request_id)
    # Get the time right now server time
    time_now = datetime.now(timezone.utc).replace(microsecond=0)
    print(time_now)

    # Get the time difference
    request_creation_time = bill_request.date_time.replace(microsecond=0)
    print(request_creation_time)
    
    # TimeDelta class base time difference between two results
    time_difference = time_now - request_creation_time 

    # print the time right now in UTC

    # print the time of request initiated
    print("Time difference is : " , time_difference)

    # Get the time difference in Minutes for more readable format
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Check if time ago is less in [30] minutes
    if minutes < 30 :
        timeleft_min = 30 - minutes
        timeleft_sec = seconds
    else:
        timeleft_min = 0
        timeleft_sec = seconds


    response = {

        "minleft" : timeleft_min, 
        "secleft" : timeleft_sec
    }

    # Return Json encoded response 
    return HttpResponse(json.dumps(response))


# API for getting companies we support with respoect to bill type
def get_companies(request, bill_type):

    companies = Company.objects.all().filter(bill_type=bill_type)
    data = serializers.serialize("json", companies)

    # Return the encoded Companies to user
    return HttpResponse (data)






























############################
# --- Helper Functions --- #
############################



# --- Get the BTC TRANSACTION details with BTC address --- #
def btc_tranx_detail(btc_address):
    # http://api.blockcypher.com/v1/btc/main/addrs/3HcGoxru2msKRcmpktDNSrAgNCB9B7Zu4V
    # Make a get request to the URL with Dynamic Address
    trx_details = requests.get( "http://api.blockcypher.com/v1/btc/main/addrs/" + btc_address ).json()
    
    # return the DICT
    return trx_details


# --- Exhange the PKR to BTC --- #
# Takes [int] as amount and return [float] results converted to BTC
def exhange_pkr_to_btc(amount):
    # First of all get the exhange rate
    
    # Make a get request to https://api.blinktrade.com/api/v1/PKR/ticker
    data = requests.get("https://api.blinktrade.com/api/v1/PKR/ticker").json()
    
    # Access and store the variable ( exchange rate )
    pkr_exhange_rate = data["buy"]
    
    print(type(pkr_exhange_rate))

    print(type(amount))

    # Convert the PKR amount to BTC
    return amount / pkr_exhange_rate


# --- Generate a new address for making payments from bitfinex --- #
# Takes [None] , return [string] newly generated address [string]
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
            'nonce':str(time.time() * 1000000), #convert to string
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

    print(bit_data)

    return bit_data['address']['address']