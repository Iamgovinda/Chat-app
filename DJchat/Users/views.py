from django.shortcuts import render
from Users.forms import LoginForm,SignupForm

# Create your views here.
def signin(request):
    signupform = SignupForm()
    return render(request,"login.html")
def signup(request):
    return render(request,"register.html")