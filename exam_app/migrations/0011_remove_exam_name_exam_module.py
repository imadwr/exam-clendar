# Generated by Django 4.2.1 on 2023-05-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0010_exam_responsable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='name',
        ),
        migrations.AddField(
            model_name='exam',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam_app.module'),
        ),
    ]
