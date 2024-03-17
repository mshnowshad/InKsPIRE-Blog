
from django.urls import path
from .views import *



urlpatterns = [
    path('signin/',signin,name="signin"),
    path('',signup,name="signup"),
    # path('signin/',signin,name="signin"),
    # path('signin/',signin,name="signin"),





]
