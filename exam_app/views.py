from django.shortcuts import render, redirect
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