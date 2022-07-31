from django.http import HttpResponse
from django.shortcuts import render,redirect

from Users.forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signin(request):
    if request.method =="POST":
        signinform = LoginForm(request.POST)
        if signinform.is_valid():
            username = signinform.cleaned_data['username']
            password = signinform.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                
                return redirect("/userdash/")
    signinform = LoginForm()
    return render(request,"Users/login.html",{'signinform':LoginForm()})


def signup(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            username = signupform.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return HttpResponse("Already exists")
            signupform.save()
            return redirect("/accounts/login/")
    signupform = SignupForm()
    return render(request,"Users/signup.html",{'signupform':SignupForm()})