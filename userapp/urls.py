from django.urls import path
from .views import userhome

urlpatterns = [
    path('user-home', userhome)

]