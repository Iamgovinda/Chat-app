from django.urls import path,include
from . import views

urlpatterns = [
    path("login/",views.signin,"signin"),
    path("signup/",views.signup,"signup")
]
