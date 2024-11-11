<template>
    <div class="modal fade" id="AddExerciseModal" tabindex="-1" aria-labelledby="AddExerciseModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="AddExerciseModalLabel">Add exercise</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="mb-3">
                        <label for="exerciseName" class="form-label">Exercise Name</label>
                        <input type="text" v-model="newExercise.exerciseName" class="form-control" id="exerciseName">
                    </div>
                    <div class="mb-3">
                        <label for="description" class="form-label">Description</label>
                        <input type="text" v-model="newExercise.description" class="form-control" aria-label="With textarea" id="description">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" v-model="newExercise.equipmentRequired" class="form-check-input" id="equipmentRequired">
                        <label class="form-check-label" for="equipmentRequired">Equipment Required</label>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="submitExercise">Add Exercise</button>
          </div>
        </div>
      </div>
    </div>
  </template>

<script>
export default {
    data() {
        return {
            newExercise : {
            exerciseName: '',
            description: '',
            equipmentRequired: false,
        }
        }  
    },

    methods: {
        submitExercise () {
            this.$emit('addExercise', this.newExercise);

            this.newExercise = {
                exerciseName: '',
                description: '',
                equipmentRequired: false,
            }
        }
    }
}

</script>