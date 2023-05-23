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

class AddExamForm(forms.Form):
    name = forms.CharField()
    salle = forms.CharField()
    group = forms.CharField()
    day = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class AddStudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    phone_number = forms.CharField()
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mn-2'