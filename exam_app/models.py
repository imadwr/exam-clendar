from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


    

class Exam(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    salle = models.CharField(max_length=10, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class StudentAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.classe}"


class Departement(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Formation(models.Model):
    name = models.CharField(max_length=30)
    departement = models.ForeignKey('Departement', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Module(models.Model):
    libelle = models.CharField(max_length=30)
    effectif = models.IntegerField()
    semestre = models.ForeignKey('Semestre', on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle



class Semestre(models.Model):
    libelle = models.CharField(max_length=30)
    date_debut = models.DateField()
    date_fin = models.DateField()
    annee_scolaire = models.CharField(max_length=30)
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle


