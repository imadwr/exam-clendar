from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def indexView(request):
    all_exams = Exam.objects.all()
    print(all_exams)
    return render(request, 'index.html', {'exams': all_exams})

def loginView(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            loginData = loginForm.cleaned_data
            user = authenticate(request, username=loginData['username'], password=loginData['password'])

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_login = True
                return render(request, 'login.html', {'form': loginForm, 'error_login': error_login})

    else:
        loginForm = LoginForm()
        return render(request, 'login.html', {'form': loginForm})
    

def logoutView(request):
    logout(request)
    return redirect('index')

def addStudentView(request):
    pass


def addExamView(request):
    if request.method == "POST":
        addExamForm = AddExamForm(request.POST)
        if addExamForm.is_valid():
            data = addExamForm.cleaned_data
            exam = Exam()
            exam.name = data["name"]
            exam.salle = data["salle"]
            exam.group = data["group"]
            exam.day = data["day"]
            exam.start_time = data["start_time"]
            exam.end_time = data["end_time"]

            exam.save()

            return redirect("index")
    else:
        addExamForm = AddExamForm()
        return render(request, 'add_exam.html', {'form': addExamForm})
    
def deleteExamView(request, id):
    exam = get_object_or_404(Exam, pk=id)
    exam.delete()
    return redirect("list_exams")



def all_Exams(request):
    all_exams = Exam.objects.all()
    out = []
    for exam in all_exams:
        out.append({
            'title': exam.name,
            'id': exam.id,
            'start': exam.start_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': exam.end_time.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)


def ListExamsView(request):
    all_exams = Exam.objects.all()
    return render(request, "list_exams.html", {"exams": all_exams})


def addStudentView(request):
    if request.method == "POST":
        addStudentForm = AddStudentForm(request.POST)
        if addStudentForm.is_valid():
            data = addStudentForm.cleaned_data
            student = Student()
            student.first_name = data["first_name"]
            student.last_name = data["last_name"]
            student.date_of_birth = data["date_of_birth"]
            student.email = data["email"]
            student.phone_number = data["phone_number"]
            student.address = data["address"]

            student.save()

            return redirect("index")
    else:
        addStudentForm = AddStudentForm()
    
    return render(request, 'add_student.html', {'form': addStudentForm})



def studentListView(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})


def updateStudentView(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list_students")
    else:
        form = UpdateStudentForm(instance=student)
    return render(request, "update_student.html", {"form": form})


def deleteStudentView(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect("list_students")


def departmentAddView(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartementForm()
    return render(request, 'department_add.html', {'form': form})


def departmentListView(request):
    departments = Departement.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


def departmentUpdateView(request, id):
    department = get_object_or_404(Departement, pk=id)
    if request.method == 'POST':
        form = DepartementForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartementForm(instance=department)
    return render(request, 'department_update.html', {'form': form})

def departmentDeleteView(request, id):
    department = get_object_or_404(Departement, pk=id)
    department.delete()
    return redirect("department_list")

