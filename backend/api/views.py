from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from .models import Workout, Exercise

class AddWorkoutForm(forms.Form):
    new_workout = forms.CharField(label='New workout')
   

class AddExerciseForm(forms.Form):
    new_exercise = forms.CharField(label='New exercise')
    difficulty = forms.IntegerField(label='difficulty', min_value=1, max_value=5)
    description = forms.TextInput(label= 'description')
    equipent_required = forms.BooleanField(label='equipment required?')




def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

def view_exercises(request):
     return JsonResponse({
         'exercises' : [exercise.as_dict() for exercise in Exercise.objects.all()]
     })


def view_workouts(request):
    return render(request, 'api/view_workouts.html', {
        'workouts' : Workout.objects.all()
    })

def add_workout(request):
    if request.method == "POST":
        form = AddWorkoutForm(request.POST)
        if form.is_valid():
            workout = form.cleaned_data['new_workout']
            newWorkout = Workout(workout_name=workout)
            newWorkout.save()
            
        else:
            return render(request, 'api/add_workout.html', {
                'form' : form
            })

    return render(request, 'api/add_workout.html', {
        'form' : AddWorkoutForm()
    })

def add_exercise(request):
    if request.method == "POST":
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.cleaned_data['new_exercise']
            newExercise = Exercise(exercise_name=exercise)
            newExercise.save()
            
        else:
            return render(request, 'api/add_exercise.html', {
                'form' : form
            })

    return render(request, 'api/add_exercise.html', {
        'form' : AddExerciseForm()
    })


