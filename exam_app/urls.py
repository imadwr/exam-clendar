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
    path('department_delete/<int:id>', departmentDeleteView, name="department_delete"),
    path('list_formations/', formationListView, name='formation_list'),
    path('formation_add/', formationAddView, name='formation_add'),
    path('formation_update/<int:id>', formationUpdateView, name="formation_update"),
    path('delete_formation/<int:id>', formationDeleteView, name="formation_delete"),
    path('list_modules/', moduleListView, name='module_list'),
    path('module_add/', moduleAddView, name='module_add'),
    path('module_update/<int:id>', moduleUpdateView, name='module_update'),
    path('modules_delete/<int:id>', moduleDeleteView, name='module_delete'),
    path('list_semester/', semesterListView, name='semester_list'),
    path('semester_add/', semesterAddView, name='semester_add'),
    path('semester_update/<int:id>', semesterUpdateView, name='semester_update'),
    path('semester_delete/<int:id>', semesterDeleteView, name='semester_delete'),
    path('list_professors/', professorListView, name="list_professors"),
    path('add_professors', addProfessorView, name="add_professors"),
    path('delete_professors/<int:id>', deleteProfessorView, name="delete_professors"),
    path('update_professors/<int:id>', updateProfessorView, name="update_professors"),
]
