from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Exam)
class examModelAdmin(admin.ModelAdmin):
    list_display = ["name", "salle", "group", "day", "start_time", "end_time"]


@admin.register(Student)
class studentModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
