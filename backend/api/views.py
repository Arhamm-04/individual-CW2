
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Workout, Exercise, WorkoutExercise
import json

def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

@csrf_exempt
def exercise_api_view(request):
    """
    this represents the api endpoint for the exercise api view which is called when a fetch is called and
      depending on the method a different outcome is produced

    when the request method is GET:
        it returns the a json response of all the exercises as a dictionary

    when the request method is POST:
        this gets the data sent through the body of the request and creates a new Exercise object and fills in all the fields using the retrieved data
        it then returns the newly created object back

    when the request method is PUT: 
        it gets the data sent through the body of the request and finds the Exercise object which needs to be updated and then changes the necessary fields and saves the new object
        it then returns the newly edited object back
    
    when the request method is DELETE:
        it gets the data sent through the body of the request and finds the exercise object to delete and then deletes 
        it then returns the json response of it being successfully deleted
    """
    if request.method == 'GET':
        return JsonResponse({
            'exercises' : [exercise.as_dict() for exercise in Exercise.objects.all()]
        })
    elif request.method == 'POST':
        data = json.loads(request.body)
        exercise = Exercise.objects.create(
            exercise_name = data['exerciseName'],
            description = data['description'],
            equipment_required = data['equipmentRequired']
        )
        return JsonResponse (exercise.as_dict(), status=200)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        exerciseName = data['name']

        exerciseObj = Exercise.objects.get(exercise_name = exerciseName)

        exerciseObj.description = data['description']
        exerciseObj.equipment_required = data['equipment_required']
        exerciseObj.save()

        return JsonResponse(exerciseObj.as_dict(), status = 200)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        name = data['name']

        exercise = Exercise.objects.get(exercise_name=name)
        exercise.delete()

        return JsonResponse({'message': 'Exercise deleted successfully.'}, status=200)

@csrf_exempt
def workout_api_view(request):
    """
    this represents the api endpoint for the workout api view which is called when a fetch is called and
      depending on the method a different outcome is produced

    when the request method is GET:
        it returns the a json response of all the workouts as a dictionary

    when the request method is POST:
        this gets the data sent through the body of the request and creates a new workout object and fills in all the fields using the retrieved data
        it then returns the newly created object back

    when the request method is PUT: 
        it gets the data sent through the body of the request and finds the workout object which needs to be updated and then changes the necessary fields and saves the new object
        it then returns the newly edited object back
    
    when the request method is DELETE:
        it gets the data sent through the body of the request and finds the workout object to delete and then deletes 
        it then returns the json response of it being successfully deleted
    """
    if request.method == 'GET':
        return JsonResponse({
            'workout' : [workout.as_dict() for workout in Workout.objects.all()]
        })
    
    elif request.method == 'POST':
        data = json.loads(request.body)

        workout = Workout.objects.create( workout_name=data['workoutName'], target_muscle_group=data['targetMuscleGroup'])

        for exercise in data['exercises']:
            exercise_name = exercise['exerciseName']
            reps = exercise['reps']
            sets = exercise['sets']
            rest_period = exercise['restPeriod']

            exerciseObj = Exercise.objects.get(exercise_name=exercise_name)

            WorkoutExercise.objects.create(
                workout=workout,
                exercise=exerciseObj,
                reps=reps,
                sets=sets,
                rest_between_exercise=rest_period
            )

        return JsonResponse(workout.as_dict(), status=201)
        
    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        name = data['name']

        workout = Workout.objects.get(workout_name=name)
        workout.delete()

        return JsonResponse({'message': 'Workout deleted successfully.'}, status=200)


@csrf_exempt
def workout_exercise_api_view(request):
    if request.method == 'GET':
        return JsonResponse({
            'workoutExercise' : [workout.as_dict() for workout in WorkoutExercise.objects.all()]
        })
    elif request.method == 'POST':
        pass
    
    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass
    else:
        return HttpResponse(status = 405)