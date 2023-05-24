# Generated by Django 4.2.1 on 2023-05-24 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0005_alter_exam_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=30)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('annee_scolaire', models.CharField(max_length=30)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.formation')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=30)),
                ('effectif', models.IntegerField()),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.semestre')),
            ],
        ),
    ]
