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
        fields=('name','salle', 'group', 'day','start_time', 'end_time')
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