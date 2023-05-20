from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name="index"),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name="logout"),
    path('addExam/', addExamView, name="add_exam"),
    path('all_exams/', all_Exams, name="all_exams"),
    path('list_exams/', ListExamsView, name="list_exams")
]
