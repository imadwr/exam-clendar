# Generated by Django 4.2.1 on 2023-05-27 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0008_salle_remove_exam_salle_exam_salle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='salle',
        ),
        migrations.AddField(
            model_name='exam',
            name='salle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam_app.salle'),
        ),
    ]
