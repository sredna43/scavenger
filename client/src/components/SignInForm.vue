<template>
    <div class="column is-8 is-offset-2">
        <h4 id="sign-inup-form">Sign in:</h4>
        <form class="login" @submit.prevent="submitForm">
            <b-field 
                label="Username">
                <b-input v-model="username"></b-input>
            </b-field>
            <b-field label="Password">
                <b-input v-model="password" type="password" password-reveal @keyup.enter.native="submitForm"></b-input>
            </b-field>

            <div class="buttons is-right">
                <b-button class="submit button is-lightgreen-invert" @click.native="clearForm">Cancel</b-button>
                <b-button class="submit button is-primary" @click.native="submitForm">Login</b-button>
            </div>
        </form>
        <br>
        <br>
    </div>
</template>

<script>
var axios = require('axios');
var passwordHash = require('password-hash');
var login_url = "http://localhost:5000/login";

export default {
    name: "SignInForm",
    data(){
        return{
            username: '',
            password: ''
        }
    },
    methods: {
        clearForm(){
            this.$parent.signIn = false;
        },
        submitForm(){
            let username = this.username;
            let password = this.password;
            axios.post(login_url, {
                username: username
            })
            .then((res) => {
                if(200 <= res.status < 300){
                    var ph = res.data[0];
                    if(passwordHash.verify(password, ph[0])){
                        console.log("Success");
                        console.log(this.$store);
                        this.$store.dispatch('auth');
                    }
                }
            });
        }
    }
}
</script>

<style scoped>

</style>