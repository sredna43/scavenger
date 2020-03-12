<template>
    <div class="columns content is-mobile">
        <div class="column is-8 is-offset-2">
            <br>
            <h1 class="title">Scavenger Hunt</h1>
            <p></p>
            <h3 class="subtitle">Last clue:</h3>
            <p>{{this.last_clue}}</p>
            <p>Enter the answer to the last clue to get your next clue:</p>
            <InputBar></InputBar>
        </div>
    </div>
</template>

<script>
import InputBar from '../components/InputBar.vue'

export default {
    name: 'Home',
    components: {
        InputBar
    },
    data() {
        return {
            last_clue: this.$route.params.input_id,
        }
    },
    created(){
        console.log(this.$route.params.input_id);
        if(this.$route.params.input_id == undefined){
            this.last_clue = "Last clue not found";
        }
    }
}
</script>