from django.http import HttpResponse

def index(request):
    return HttpResponse("Father hua hua ")

# --- MERCHENT LOGIN --- #

# .. Get the Information from user
# .. Validate the information about the user
# .. Make sure if user is pending or block 
# .. If the user is blocked or pending show them a error message

# --- MERCHENT REGISTERATION ---#

# .. Get all the information via Post Request through HttpRequestObject
# .. Validate and Store the Information into Database
# .. Flash the message that Registration request sent and waiting for approval from Admin

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

