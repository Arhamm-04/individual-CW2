<template>
    <div class="modal fade" id="AddWorkoutModal" tabindex="-1" aria-labelledby="AddWorkoutModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="AddWorkoutModalLabel">Add Workout</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3">
                            <label for="workoutName" class="form-label">Workout Name</label>
                            <input type="text" v-model="newWorkout.workoutName" class="form-control" id="workoutName">
                        </div>
                        <div class="mb-3">
                            <label for="targetMuscleGroup" class="form-label">Target Muscle Group</label>
                            <input type="text" v-model="newWorkout.targetMuscleGroup" class="form-control" id="targetMuscleGroup">
                        </div>

                        <div class="border-bottom border-top pb-2 pt-2">
                            <label>Exercises</label>
                            <select class="form-select" v-model="newExercise.exerciseName" aria-label="Default select">
                                <option v-for="(exercise, index) in exercises" :key="index" :value="exercise.name">
                                    {{ exercise.name }}
                                </option>
                            </select>
                            <label class="form-label">Reps</label>
                            <input type="number" v-model="newExercise.reps" class="form-control">

                            <label class="form-label">Sets</label>
                            <input type="number" v-model="newExercise.sets" class="form-control">

                            <label class="form-label">Rest Period (seconds)</label>
                            <input type="number" v-model="newExercise.restPeriod" class="form-control">

                            <button type="button" class="btn btn-secondary mt-2" @click="addExerciseField">
                                Add Exercise
                            </button>
                        </div>

                        <h6 class="mt-4">Exercises Added</h6>
                        <div v-if="workoutExercises.length" class="mt-2">
                            <div v-for="(exercise, index) in workoutExercises" :key="index" class="card mb-2">
                                <div class="card-body">
                                    <h5 class="card-title">{{ exercise.exerciseName }}</h5>
                                    <p class="card-text">Reps: {{ exercise.reps }}, Sets: {{ exercise.sets }}, Rest: {{ exercise.restPeriod }} seconds</p>
                                    <button type="button" class="btn btn-danger" @click="removeExercise(index)">
                                        Delete
                                    </button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="submitWorkout">Add Workout</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        exercises: Array 
    },
    data() {
        return {
            newWorkout: {
                workoutName: '',
                targetMuscleGroup: '',
            },
            newExercise: {
                exerciseName: '',
                reps: 0,
                sets: 0,
                restPeriod: 0,
            },
            workoutExercises: [] 
        };
    },
    methods: {
        addExerciseField() {
            this.workoutExercises.push({...this.newExercise})

            this.newWorkout = {
                workoutName: '',
                targetMuscleGroup: '',
            };
        },
        removeExercise(index) {
            this.workoutExercises.splice(index, 1);
        },

        submitWorkout() {
            const workoutData = {
                workoutName: this.newWorkout.workoutName,
                targetMuscleGroup: this.newWorkout.targetMuscleGroup,
                exercises: this.workoutExercises,
            };

            this.$emit('addWorkout', workoutData);

            this.newWorkout = {
                workoutName: '',
                targetMuscleGroup: '',
            };
            this.workoutExercises = []; 
        }
    }
};
</script>

<style scoped>

</style>
