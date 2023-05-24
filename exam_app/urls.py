from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name="index"),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name="logout"),
    path('addExam/', addExamView, name="add_exam"),
    path('all_exams/', all_Exams, name="all_exams"),
    path('list_exams/', ListExamsView, name="list_exams"),
    path('delete_exam/<int:id>', deleteExamView, name="delete_exam"),
    path('addstudent/', addStudentView, name="add_student"),
    path('list_students/', studentListView, name="list_students"),
    path('delete_student/<int:id>', deleteStudentView, name="delete_student"),
    path('update_student/<int:id>', updateStudentView, name="update_student"),
    path('list_departments/', departmentListView, name='department_list'),
    path('department_add/', departmentAddView, name='department_add'),
    path('department_update/<int:id>', departmentUpdateView, name="department_update"),
    path('department_delete/<int:id>', departmentDeleteView, name="department_delete")
]
