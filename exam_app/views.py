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

            all_exams = Exam.objects.all()

            for ex in all_exams:
                if exam.name == ex.name and exam.group == ex.group:
                    error = "Exam already programmed for this group"
                    return render(request, 'add_exam.html', {'form': addExamForm, 'error': error})

                if ex.salle == exam.salle and ex.day == exam.day:
                    if not ((exam.start_time < ex.start_time and exam.end_time < ex.start_time) or (exam.start_time > ex.end_time and exam.end_time > ex.end_time)):
                        error = "Classroom not disponible in this day and time"
                        return render(request, 'add_exam.html', {'form': addExamForm, 'error': error})


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


def formationAddView(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formation_list')
    else:
        form = FormationForm()
    return render(request, 'formation_add.html', {'form': form})

def formationListView(request):
    formations = Formation.objects.all()
    return render(request, 'formation_list.html', {'formations': formations})


def formationUpdateView(request, id):
    formation = get_object_or_404(Formation, pk=id)
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('formation_list')
    else:
        form = FormationForm(instance=formation)
    return render(request, 'formation_update.html', {'form': form})

def formationDeleteView(request, id):
    formation = get_object_or_404(Formation, pk=id)
    formation.delete()
    return redirect("formation_list")


def moduleListView(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})


def moduleAddView(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm()
    return render(request, 'module_add.html', {'form': form})

def moduleUpdateView(request, id):
    module = get_object_or_404(Module, pk=id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm(instance=module)
    return render(request, 'module_update.html', {'form': form, 'module': module})

def moduleDeleteView(request, id):
    module = get_object_or_404(Module, pk=id)
    module.delete()
    return redirect("module_list")


def semesterListView(request):
    semestres = Semestre.objects.all()
    return render(request, 'semester_list.html', {'semestres': semestres})


def semesterAddView(request):
    if request.method == 'POST':
        form = SemestreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemestreForm()
    return render(request, 'semester_add.html', {'form': form})

def semesterUpdateView(request, id):
    semestre = get_object_or_404(Semestre, pk=id)
    if request.method == 'POST':
        form = SemestreForm(request.POST, instance=semestre)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemestreForm(instance=semestre)
    return render(request, 'semester_update.html', {'form': form})

def semesterDeleteView(request, id):
    semester = get_object_or_404(Semestre, pk=id)
    semester.delete()
    return redirect("semester_list")


def addProfessorView(request):
    if request.method == "POST":
        addProfessorForm = ProfessorForm(request.POST)
        if addProfessorForm.is_valid():
            addProfessorForm.save()

            return redirect("index")
    else:
        addProfessorForm = ProfessorForm()

    return render(request, 'add_professor.html', {'form': addProfessorForm})


def professorListView(request):
    professors = Professor.objects.all()
    return render(request, 'list_professor.html', {'professors': professors})


def updateProfessorView(request, id):
    professor = get_object_or_404(Professor, id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect("list_professors")
    else:
        form = ProfessorForm(instance=professor)
    return render(request, "update_professor.html", {"form": form})


def deleteProfessorView(request, id):
    professor = get_object_or_404(Professor, pk=id)
    professor.delete()
    return redirect("list_professors")