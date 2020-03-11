<template>
    <div>
        <h1>Next clue:</h1>
        <p>{{clue}}</p>
        <br>
        <button class="button block" @click="isActive1 = !isActive1">Hint 1</button>
        <b-notification :active.sync="isActive1" aria-close-label="Close Notification">
            {{hint1}}
        </b-notification>
        <br>
        <button class="button block" @click="isActive2 = !isActive2">Hint 2</button>
        <b-notification :active.sync="isActive2" aria-close-label="Close Notification">
            {{hint2}}
        </b-notification>
        <br>
        <router-link to='/'>Back</router-link>
    </div>
</template>

<script>
//import axios from 'axios';
var urlCrypt = require('url-crypt')('SJx3VCntc_{5E&%~mK$@L8(8Rw?{zRj?aZ5/^DzN}+/');
export default {
    name: 'Clue',
    data() {
        return {
            clue: urlCrypt.decryptObj(this.$route.params.clue_id).clue,
            hint1: urlCrypt.decryptObj(this.$route.params.clue_id).hint1,
            hint2: urlCrypt.decryptObj(this.$route.params.clue_id).hint2,
            isActive1: false,
            isActive2: false,
        };
    },
    methods: {
    }
}
</script>