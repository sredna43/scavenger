<template>
<div>
    <div class="columns content is-mobile">
        <div class="column is-10 is-offset-1">
            <br>
            <h1 class="title">Scavenger Hunt</h1>
            <p>Hello and welcome to the St. Olaf Band Scavenger hunt!</p>
            <p>To get started, please eiter sign in or sign up.</p>
            <div class="buttons">
                <b-button class="submit button is-primary-invert" v-scroll-to="{element: '#sign-inup-form', duration: 750}" @click.native="signInPress" expanded>Sign In</b-button>
                <b-button class="submit button is-primary" v-scroll-to="{element: '#sign-inup-form', duration: 750}" @click.native="signUpPress" expanded>Sign Up</b-button>
            </div>
        </div>
    </div>
    <br>
    <div class="columns content is-mobile">
        <div class="column is-10 is-offset-1">
            <sign-up-form v-if="signUp"></sign-up-form>
            <sign-in-form v-if="signIn"></sign-in-form>
        </div>
    </div>
</div>
    
</template>

<script>
import SignUpForm from '../components/SignUpForm.vue'
import SignInForm from '../components/SignInForm.vue'
export default {
    name: 'Home',
    components: {
        SignUpForm,
        SignInForm
    },
    data() {
        return {
            signIn: false,
            signUp: false,
        }
    },
    methods:{
        signInPress(){
            this.signIn = true;
            this.signUp = false;
        },
        signUpPress(){
            this.signIn = false;
            this.signUp = true;
        }
    }
}
</script>