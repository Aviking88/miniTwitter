from django.shortcuts import render

from .models import userData, tweetData
from django.http import Http404
import datetime

available = userData.objects.values('userName', 'email')

def getTweettData():
    available = userData.objects.values('userName', 'email')
    tweetDataobj = tweetData.objects.all()
    tweetDataobj = tweetDataobj[::-1]
    return tweetDataobj



#this method will call upon index request
def index(request):
    return render(request, 'index.html')

#this method will call upon user Registration
def welcome(request):
    ud = userData()
    d = request.POST.get("username")
    ud.userName = request.POST.get("username")
    ud.dob = request.POST.get("dob")
    ud.email = request.POST.get("email")
    ud.password = request.POST.get("password")
    ud.save()
    dataobj = userData.objects.get(userName=d)
    updateTweettData()
    return render(request, 'welcome.html',
                  {'dataobj': dataobj, 'tweetDataobj': getTweettData(),'available': available})

#this method will call upon user Login
def welcomeUser(request):
    d = request.POST.get("email")
    p = request.POST.get("password")
    dataobj = None
    try:
        dataobj = userData.objects.get(email=d)
        if (p == dataobj.password):
            available = userData.objects.values('userName', 'email')
        else:
            raise Http404('Requested user not found. or Wrong Password')
    except:
        raise Http404('Requested user not found.')

    return render(request, 'welcome.html',
                  {'dataobj': dataobj, 'tweetDataobj': getTweettData(),'available': available})



#this method will call upon tweetPost
def tweet(request):
    ud = tweetData()
    d = request.POST.get("userNameTweet")
    ud.userName = request.POST.get("userNameTweet")
    ud.name = request.POST.get("NameTweet")
    ud.message = request.POST.get("msg")

    ud.tweettime = datetime.datetime.now()
    ud.save()
    dataobj = userData.objects.get(email=d)

    return render(request, 'welcome.html',
                  {'dataobj': dataobj, 'tweetDataobj': getTweettData(),'available': available})

#this method will call upon tweetDelete
def deleteTweet(request):
    id = request.POST.get("tweetID")
    d = request.POST.get("userID")
    tweetData.objects.filter(msgID=id).delete()
    available = userData.objects.values('userName', 'email')
    dataobj = userData.objects.get(email=d)
    return render(request, 'welcome.html',
                  {'dataobj': dataobj, 'tweetDataobj': getTweettData(),'available': available})
