from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def indexView(request):
    return render(request, 'index.html')

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