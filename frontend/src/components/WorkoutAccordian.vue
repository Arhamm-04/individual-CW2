<template>
    <div class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item" v-for="(workout, workoutIndex) in workout" :key="workoutIndex">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" :data-bs-toggle="'collapse'" :data-bs-target="'#flush-collapse' + workoutIndex" :aria-expanded="false" :aria-controls="'flush-collapse' + workoutIndex">
                    {{ workout.name }}
                </button>
                <button @click="removeWorkout(workout.name)">
                    remove
                </button>
            </h2>
        <div :id="'flush-collapse' + workoutIndex" class="accordion-collapse collapse" :data-bs-parent="'#accordionFlushExample'">
          <div class="accordion-body">
            <h5>target muscle group:</h5>
            <p>{{ workout.target_muscle_group }}</p>
            <h5>exercises:</h5>
            <ul>
                <li v-for="(exercise, exerciseIndex) in workout.exercises" :key="exerciseIndex">
                {{ exercise.exercise.name }}
                <button class="btn btn-primary" type="button" data-bs-toggle="modal" :data-bs-target="'#exerciseModal' + workoutIndex + '-' + exerciseIndex">
                    See Details
                </button>

                <div :id="'exerciseModal' + workoutIndex + '-' + exerciseIndex" class="modal fade" tabindex="-1" aria-labelledby="'exerciseModalLabel' + workoutIndex + '-' + exerciseIndex" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" :id="'exerciseModalLabel' + workoutIndex + '-' + exerciseIndex">{{ exercise.exercise.name }} Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <p><strong>Reps:</strong> {{ exercise.reps }}</p>
                                <p><strong>Sets:</strong> {{ exercise.sets }}</p>
                                <p><strong>Rest Period:</strong> {{ exercise.rest_period }} seconds</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
                </li>
            </ul>
            <h5>date made:</h5>
            <p>{{ workout.date }}</p>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    props: {
        workout: Array
    },

    methods: {
        removeWorkout (name) {
            this.$emit('removeWorkout', name)
        }
    }
}
</script>
