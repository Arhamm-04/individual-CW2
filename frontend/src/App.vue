<template data-bs-theme="dark">
    <div class="container pt-3">
        <div class="h1 text-center border rounded p-2 mb-3">
            {{ title }}
        </div>

        <div>
            <ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
                <li class="nav-item" v-for="tab in tabs" :key="tab" role="presentation">
                    <button class="nav-link" :class="{ active: activeTab === tab }" @click="selectTab(tab)">
                    {{ tab }}
                    </button>
                </li>
            </ul>
        </div>
        
        <div class="tab-content">
            <div v-if="activeTab === 'exercises'" class="tab-pane fade show active">
                <ExerciseAccordian :exercises = exercises @removeExercise="DELExercise" @updateExercise="PUTExercise"/>
            </div>
            <div v-else-if="activeTab === 'workouts'" class="tab-pane fade show active">
                <WorkoutAccordian :workout=workouts @removeWorkout="DELWorkout" />
            </div>
        </div>

        <div>
            <button v-if="activeTab === 'exercises'" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#AddExerciseModal">
                Add exercise
            </button>
            <button v-else-if="activeTab === 'workouts'" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#AddWorkoutModal">
                Add workout
            </button>
        </div>

        
        
        <AddExerciseModal @addExercise="POSTExercise" />
        <AddWorkoutModal @addWorkout="POSTWorkout" :exercises=exercises />
      
        

    </div>
  </template>
  
<script>
import AddExerciseModal from './components/AddExerciseModal.vue';
import AddWorkoutModal from './components/AddWorkoutModal.vue';
import ExerciseAccordian from './components/ExerciseAccordian.vue';
import WorkoutAccordian from './components/WorkoutAccordian.vue';







export default {
    components: {
        WorkoutAccordian,
        ExerciseAccordian,
        AddExerciseModal,
        AddWorkoutModal,
    },

    data() {
        return {
            title: 'Workout Maker',
            newExercise : '',
            exercises : [] ,
            workouts : [],
            tabs : ['exercises', 'workouts'],
            activeTab : 'exercises',
        }
    },

    methods : {
        selectTab (tab) {
            this.activeTab = tab
        },

        async POSTExercise (newExercise) {
            try {
                const POST_exercise_response = await fetch('http://localhost:8000/api/exercise-api-view', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(newExercise)
                })

                if (!POST_exercise_response.ok) {
                    throw new Error('Network response was not ok');
                }

                const POST_exercise_response_data = await POST_exercise_response.json()
                this.exercises.push( POST_exercise_response_data)

            } catch (error) {
                console.log(error)
            }
        },

        async PUTExercise (updatedExercise) {
            try {
                const PUT_exercise_response = await fetch('http://localhost:8000/api/exercise-api-view', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(updatedExercise)
                })

                if (!PUT_exercise_response.ok) {
                    throw new Error('Network response was not ok');
                }

                const PUT_exercise_response_data = await PUT_exercise_response.json()
                this.exercises = this.exercises.map(exerciseToChange => exerciseToChange.name === PUT_exercise_response_data.name ? PUT_exercise_response_data : exerciseToChange);

            } catch (error) {
                console.log(error)
            }
        },

        async POSTWorkout (workoutData) {
            try {
                const POST_workout_response = await fetch('http://localhost:8000/api/workout-api-view', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(workoutData)
                })

                if (!POST_workout_response.ok) {
                    throw new Error('Network response was not ok');
                }   

                const POST_workout_response_data = await POST_workout_response.json()
                this.workouts.push(POST_workout_response_data)

            } catch (error) {
                console.log(error)
            }
        },

        async DELExercise (exercise_name) {
            try {
                const DEL_exercise_response = await fetch('http://localhost:8000/api/exercise-api-view', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({name: exercise_name})
                })

                if (!DEL_exercise_response.ok) {
                    throw new Error('Network response was not ok');
                }

                const DEL_exercise_response_data = await DEL_exercise_response.json()
                if (DEL_exercise_response_data.message === 'Exercise deleted successfully.') {
                    console.log('works')
                    this.exercises = this.exercises.filter(exercise => exercise.name != exercise_name)

                    this.workouts.forEach( workout => {workout.exercises = workout.exercises.filter(workout_exercise => workout_exercise.exercise.name != exercise_name)})
                }
            } catch (error) {
                console.log(error)
            }
        },
        async DELWorkout (workoutName) {
            try {
                const DEL_workout_response = await fetch('http://localhost:8000/api/workout-api-view', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({name: workoutName})
                })

                if (!DEL_workout_response.ok) {
                    throw new Error('Network response was not ok');
                }

                const DEL_workout_response_data = await DEL_workout_response.json()
                if (DEL_workout_response_data.message === 'Workout deleted successfully.') {
                    console.log('worked')
                    this.workouts = this.workouts.filter(workout => workout.name != workoutName)
                }

            } catch (error) {
                console.log(error)
            }
        }
    },

    async mounted() {
        try {
            const exercise_response = await fetch('http://localhost:8000/api/exercise-api-view');
            const workout_response = await fetch('http://localhost:8000/api/workout-api-view');

            if (!exercise_response.ok || !workout_response.ok) {
                throw new Error('Network response was not ok');
            }
            const exercise_response_data = await exercise_response.json();
            const workout_response_data = await workout_response.json();
            this.exercises = exercise_response_data.exercises
            this.workouts = workout_response_data.workout
            
            
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }
}
</script>
