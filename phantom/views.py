from datetime import datetime
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from string import replace
import subprocess
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import Http404
 

def home(request):
    
    subprocess.call(["say","welcome to phantom"])
    return render (request,"home.html")
@csrf_exempt
def checkpassword(request):
    password = request.POST["password"] 
    if password == "12345":
        return HttpResponse("http://www.google.com")
    else:
        raise Http404("Bad Password")
        
