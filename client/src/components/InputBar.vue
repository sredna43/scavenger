<template>
    <form v-on:keyup="submitForm" @submit.stop.prevent>
    <b-field grouped>
    <b-input 
        v-model="passphrase"
        placeholder="Answer..."
        type="text"
        expanded>
    </b-input>
    </b-field>
    <b-button class="submit button is-lightgreen" @click.native="submitButton" expanded>Go!</b-button>
    </form>
</template>

<script>
var urlCrypt = require('url-crypt')('SJx3VCntc_{5E&%~mK$@L8(8Rw?{zRj?aZ5/^DzN}+/');
var ip = 'localhost'
import axios from 'axios';
export default {
    name: 'InputBar',
    data () {
        return {
            passphrase: '',
            clue: '',
        };
    },
    methods: {
        submitForm(e) {
            if (e.keyCode === 13){
                var url = 'http://'+ip+':5000/clue';
                axios.post(url, {passphrase: this.passphrase})
                .then((res)=>{
                    console.log("res " + res)
                    console.log("res.data " + res.data)
                    this.clue = res.data;
                    if(this.clue != "Not Found"){
                        console.log("clue_data: ");
                        console.log(this.clue);
                        this.$router.push("/clue/"+urlCrypt.cryptObj(this.clue));
                    }
                    else{
                        this.$buefy.dialog.alert({
                        title: "Bummer!",
                        message: "Sorry, that's not a clue...",
                        confirmText: "Try again"
                    });
                    }
                })
                .catch((error => {
                    console.error(error);
                    this.$buefy.dialog.alert({
                        type: "is-danger",
                        title: "Whoops",
                        message: "Something is up with the server",
                        confirmText: "Go Back"
                    });
                }));
            }
        },
        submitButton(){
            var url = 'http://'+ip+':5000/clue';
            axios.post(url, {passphrase: this.passphrase})
            .then((res)=>{
                this.clue = res.data;
                if(this.clue != "Not Found"){
                    this.$router.push("/clue/"+urlCrypt.cryptObj(this.clue));
                }
                else{
                    this.$buefy.dialog.alert({
                        title: "Bummer!",
                        message: "Sorry, that's not a clue...",
                        confirmText: "Try again"
                    });
                }
            })
            .catch((error => {
                console.error(error);
                this.$buefy.dialog.alert({
                        type: "is-danger",
                        title: "Whoops",
                        message: "Something is up with the server",
                        confirmText: "Go Back"
                });
            }));
        },
    },
};
</script>