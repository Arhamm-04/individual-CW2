from django.db import models
from datetime import date
# Create your models here.

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=200)  
    description = models.TextField()
    difficulty = models.IntegerField()
    equipment_required = models.BooleanField()

    def __str__(self) -> str:
        return self.exercise_name
    
    def as_dict(self):
        return{
            'id' : self.id,
            'name' : self.exercise_name,
            'description' : self.description,
            'difficulty' : self.difficulty
        }

class Workout(models.Model):
    workout_name = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self) -> str:
        return self.workout_name
    
    def as_dict(self):
        return{
            'id' : self.id,
            'name' : self.workout_name,
            'date' : self.date,
        }
    
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()

     