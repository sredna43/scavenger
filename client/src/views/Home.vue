<template>
    <div class="columns content">
        <div class="column is-8 is-offset-2">
            <br>
            <h1 class="title">Scavenger Hunt</h1>
            <p>Enter the answer to the last clue to get your next clue:</p>
            <InputBar></InputBar>
            <b-button class="on-bottom" expanded>I'm new here</b-button>
        </div>
    </div>
</template>

<script>
import InputBar from '../components/InputBar.vue'

export default {
    name: 'Home',
    components: {
        InputBar
    }
}
</script>