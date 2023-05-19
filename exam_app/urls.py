from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name="index"),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name="logout")
]
