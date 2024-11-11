from django.db import models
from datetime import date
# Create your models here.

class Exercise(models.Model):
    """ this is a representation of the exercise model 
    this has the fields which holds the exercises name its description and whether equipment is required
    
    """
    exercise_name = models.CharField(max_length=200, unique=True)  
    description = models.TextField(default='')
    equipment_required = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        """
            this returns exercise name when its called as string
        """
        return self.exercise_name
    
    def as_dict(self):
        """
            this converts the model and all its fields into a dictionary
        """
        return{
            'id' : self.id,
            'name' : self.exercise_name,
            'description' : self.description,
            'equipment_required' : self.equipment_required,
        }

class Workout(models.Model):
    """
    this is a representation of the workout model which has fields to represent the workouts,
    name, the date it was made, the target muscle group, and the different exercises associated with it
    using the through table to do this
    """
    workout_name = models.CharField(max_length=200, unique=True)
    date = models.DateField(default=date.today)
    target_muscle_group = models.TextField(default='')
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self) -> str:
        """
            this returns the workout name when its called as a string
        """
        return self.workout_name
    
    def exercise_with_through(self):
        """
            this function goes through the through table and filters just for the workout it is and then adds to a list
            the exercise and all the extra information from the through table to this list as an object
        """
        workout_exercises = WorkoutExercise.objects.filter(workout=self)
        exercises_with_through =[]

        for workout_exercise in workout_exercises:
            exercise_data = {
                'exercise' : workout_exercise.exercise.as_dict(),
                'reps' : workout_exercise.reps,
                'sets' : workout_exercise.sets,
                'rest_period' : workout_exercise.rest_between_exercise,
            }
        
            exercises_with_through.append(exercise_data)

        return exercises_with_through
    
    def as_dict(self):
        """
            this returns the model as a dictionary with the all the exercises using the exercise_with_through function
            to get all the other information
        """
        return {
            'id': self.id,
            'name': self.workout_name,
            'date': self.date,
            'target_muscle_group': self.target_muscle_group,
            'exercises': self.exercise_with_through(),
        }
    
class WorkoutExercise(models.Model):
    """
        this represents the connection between the other 2 models as a through model and holds the extra information between teh 2
    """
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rest_between_exercise = models.IntegerField(default=5)
    reps = models.IntegerField(default=1)
    sets = models.IntegerField(default=1)

    def __str__(self):
        """
            this returns the name and its fields when its called as a string
        """
        return f"{self.exercise.exercise_name} in {self.workout.workout_name} (Rest: {self.rest_between_exercise} mins)(Reps: {self.reps}, Sets: {self.sets})"

    def as_dict(self):
        """
            this returns the models information as a dictionary
        """
        return {
            'id': self.id,
            'workout': self.workout.as_dict(), 
            'exercise': self.exercise.as_dict(),  
            'rest_between_exercise': self.rest_between_exercise,
            'reps' : self.reps,
            'sets' : self.sets,
            
        }

     