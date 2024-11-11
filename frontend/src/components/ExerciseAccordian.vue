<template>
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item" v-for="(exercise, index) in exercises" :key="index">
        <h2 class="accordion-header">
          <button
            class="accordion-button collapsed"
            type="button"
            :data-bs-toggle="'collapse'"
            :data-bs-target="'#flush-collapse' + index"
            :aria-expanded="false"
            :aria-controls="'flush-collapse' + index"
          >
            {{ exercise.name }}
          </button>
          <button @click="removeExercise(exercise.name)">
            Remove
          </button>

          <button
            type="button"
            class="btn btn-primary"
            :data-bs-toggle="'modal'"
            :data-bs-target="'#editExerciseModal' + index"
          >
            Edit
          </button>
        </h2>
        
        <div :id="'flush-collapse' + index" class="accordion-collapse collapse" :data-bs-parent="'#accordionFlushExample'">
          <div class="accordion-body">
            <h5>Description:</h5>
            <p>{{ exercise.description }}</p>
            <h5>Equipment Required:</h5>
            <p>{{ exercise.equipment_required ? 'Yes' : 'No' }}</p>
          </div>
        </div>

        <div
          :id="'editExerciseModal' + index"
          class="modal fade"
          tabindex="-1"
          aria-labelledby="editExerciseModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Edit {{ exercise.name }}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="mb-3">
                  <label for="description" class="form-label">Description</label>
                  <input
                    type="text"
                    v-model="exercise.description"
                    class="form-control"
                    aria-label="With textarea"
                    :id="'description' + index"
                  />
                </div>
                <div class="form-check">
                  <input
                    type="checkbox"
                    v-model="exercise.equipment_required"
                    class="form-check-input"
                    :id="'equipment_required' + index"
                  />
                  <label class="form-check-label" for="equipmentRequired">Equipment Required</label>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="saveChanges(exercise)">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      exercises: Array,
    },
    methods: {
      removeExercise(exercise_name) {
        this.$emit('removeExercise', exercise_name);
      },
      saveChanges(updatedExercise) {
        this.$emit('updateExercise', updatedExercise);
      },
    },
  };
  </script>
  