<template>
    <table class="table">
        <thead>
            <tr>
                <th>#</th>
                <th>Exercise name</th>
                
                <th>equipment required</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(exercise, index) in exercises" :key="index">
                <td>{{ exercise.id }}</td>
                <td>{{ exercise.name }}</td>
                <td>{{ exercise.reps }}</td>
                <td>{{ exercise.sets }}</td>
                <td>{{ exercise.equipment_required }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        exercises: Array()
    }
}
</script>