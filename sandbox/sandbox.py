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