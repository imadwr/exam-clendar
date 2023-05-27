from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class AddExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields=('name','salle', 'group','responsable', 'day','start_time', 'end_time')
        widgets = {
            'start_time': TimeInput,
            'end_time': TimeInput,
            'day': DateInput
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=('first_name','last_name', 'date_of_birth', 'email','phone_number', 'address', 'group')
        widgets = {
            'date_of_birth': DateInput,
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields=('first_name','last_name', 'email','phone_number')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'group']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['name', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['name', 'departement']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['libelle', 'effectif', 'semestre']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['libelle', 'date_debut', 'date_fin', 'annee_scolaire', 'formation']
        widgets = {
            'date_debut': DateInput,
            'date_fin': DateInput
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'