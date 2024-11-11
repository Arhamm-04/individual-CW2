<template>
    <table class="table">
        <thead>
            <tr>
                <th>#</th>
                <th>workout name</th>
                <th>target muscle group</th>
                <th>date</th>
                <th>exercise</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(workout, index) in workout" :key="index">
                <td>{{ workout.id }}</td>
                <td>{{ workout.name }}</td>
                <td>{{ workout.target_muscle_group }}</td>
                <td>{{ workout.date }}</td>
                <td v-for="(exercise, index2) in workout.exercises" :key="exercise.id">{{exercise.name }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        workout: Array()
    }
}
</script>