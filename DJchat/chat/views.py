from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"chat/home.html")

def userdash(request):
    return render(request,"chat/userdash.html")