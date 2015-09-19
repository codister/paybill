from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pb.forms import UserForm, MerchentForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "index.html")


@login_required
def settings(request):
    if request.method == 'POST':
        merchent_form = MerchentForm()
        if merchent_form.is_valid(): 
            merchent = merchent_form.save(commit=False)
            merchent.user = request.user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()



    return render(request,
            'setting.html',
            {'merchent_form': merchent_form })











































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
            return HttpResponse("Invalid login details supplied.")
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

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'pb/register.html',
            {'user_form': user_form, 'registered': registered} )
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

# --- Track Transfers --- #

# --- Requests --- #

