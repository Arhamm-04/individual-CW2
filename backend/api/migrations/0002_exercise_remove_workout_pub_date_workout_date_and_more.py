# Generated by Django 5.1.2 on 2024-10-27 11:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='workout',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workout')),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(through='api.WorkoutExercise', to='api.exercise'),
        ),
    ]