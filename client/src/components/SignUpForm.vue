<template>
    <section class="column is-8 is-offset-2">
        <h4>Sign up:</h4>
        <b-field label="Name">
            <b-input v-model="name"></b-input>
        </b-field>
        <b-field 
            id="sign-inup-form"
            label="Username" 
            :type=checkUser.success
            :message=checkUser.message>
            <b-input v-model="username" @input=checkUsername maxlength="20"></b-input>
        </b-field>
        <b-field 
            label="Password"
            :type=checkPass.success
            :message=checkPass.message>
            <b-input v-model="password" type="password" password-reveal @focus="checkUsername" @input="checkPassword" maxlength="30"></b-input>
        </b-field>
        <b-field
            label="Re-Type Password"
            :type=checkPass.matchsuccess
            :message=checkPass.matchmessage>
            <b-input v-model="passmatch" type="password" password-reveal @input="checkPassword" @keyup.enter.native="submitForm" maxlength="30"></b-input>
        </b-field>
        <div class="buttons is-right">
            <b-button class="submit button is-lightgreen-invert" @click.native="clearForm">Cancel</b-button>
            <b-button class="submit button is-primary" @click.native="submitForm">Sign Up</b-button>
        </div>
        <br>
        <br>
    </section>
</template>

<script>
<<<<<<< HEAD
var axios = require('axios');
var passwordHash = require('password-hash');
axios.defaults.headers.common['key'] = '317f7911-4b82-4d4f-adb6-9bd6fef3d84f';
var url = 'http://localhost:5000'
import store from '../store'
=======
//var passwordHash = require('password-hash');
>>>>>>> 7fc7bab39eb4ea2eb255248ed1ec22f7a2a149ec
export default {
    name: "SignUpForm",
    data() {
        return {
            checkUser: {
<<<<<<< HEAD
                success: "is-danger",
                message: "Username must be at least 4 characters",
=======
                success: "",
                message: "",
>>>>>>> 7fc7bab39eb4ea2eb255248ed1ec22f7a2a149ec
                taken: false,
            },
            checkPass: {
                success: "",
                message: ['Password must have at least 8 characters', "(Also don't use an important one...)"],
                valid: false,
                match: false,
                matchmessage: "Passwords must match",
                matchsuccess: "",
            },
            username: '',
            name: '',
            password: '',
            passmatch: '',
            TakenNames: [],
        }
    },
    methods: {
        checkUsername(){
            var TakenNames = this.TakenNames;
                if(!TakenNames.includes(this.username) && this.username.length > 3){
                this.checkUser.success = "is-success";
                this.checkUser.message = "";
                this.checkUser.taken = false;
<<<<<<< HEAD
                }
                else{
                    if(this.username.length <= 3 && !TakenNames.includes(this.username)){
                        this.checkUser.success = "is-danger";
                        this.checkUser.message = "Username must be at least 4 characters";
                        this.checkUser.taken = true; //I think I hackily made this the check for posting an add-user
                    }
                    if(this.username.length > 3 && TakenNames.includes(this.username)){
                        this.checkUser.success = "is-danger";
                        this.checkUser.message = "Username taken";
                        this.checkUser.taken = true;
                    }
                    if(this.username.length <= 3 && TakenNames.includes(this.username)){
                        this.checkUser.success = "is-danger";
                        this.checkUser.message = ["Username taken", "Username must be at least 4 characters"];
                        this.checkUser.taken = true;
                    }
                }
=======
            }
            else {
                this.checkUser.success = "is-danger";
                this.checkUser.message = "Username taken or is too short - must be 4 characters";
                this.checkUser.taken = true;
            }
>>>>>>> 7fc7bab39eb4ea2eb255248ed1ec22f7a2a149ec
        },
        checkPassword(){
            if(this.password.length < 8){
                this.checkPass.success = "is-danger";
                this.checkPass.message = ['Password is too short','Password must have at least 8 characters'];
            } 
            else {
                this.checkPass.success = "is-success";
                this.checkPass.message = "";
                this.checkPass.valid = true;
            }
            if(this.password != this.passmatch){
                this.checkPass.match = false;
                this.checkPass.matchmessage = "Passwords must match";
                this.checkPass.matchsuccess = "is-danger";
            }
            else {
                this.checkPass.match = true;
                this.checkPass.matchmessage = "";
                this.checkPass.matchsuccess = "is-success";
            }
        },
        clearForm(){
            this.name = '';
            this.username = '';
            this.password = '';
            this.$parent.signUp = false;
        },
        submitForm(){
            var adduser_url = url + '/add_user'
            this.checkUsername();
            this.checkPassword();
            if(!this.checkUser.taken && this.checkPass.valid && this.checkPass.match){
                axios.post(adduser_url, {
                    name: this.name,
                    username: this.username,
                    passhash: passwordHash.generate(this.password),
                    last_clue_id: 1
                })
                .then((res) => {
                    if(200 <= res.status < 300){
                        this.$buefy.toast.open("Signed up successfully");
                        this.$router.push({name: 'NewUser', params: {user: this.name}});
                        store.dispatch("authenticate");
                    }
                    else{
                        this.$buefy.dialog.alert({
                            type: "is-danger",
                            title: "Whoops",
                            message: "Something is up with the server",
                            confirmText: "Go Back"
                        });
                    }
                    
                });
                
            }
            else {
                var errmsg = [];
                if(this.password != this.passmatch){
                    errmsg.push("Passwords must match");
                }
                if(!this.checkPass.valid){
                    errmsg.push("Password must be 8 characters long")
                }
                if(this.checkUser.taken){
                    errmsg.push("Username taken")
                }
                this.$buefy.dialog.alert({
                                type: "is-danger",
                                title: "Error",
                                message: "Error: " + errmsg.join(', '),
                                confirmText: "Go Back"
                        });
            }
        }
    },
    created(){
        var user_url = url + '/get_users'
        console.log(user_url);
        axios.get(user_url)
        .then((res) => {
            this.TakenNames = res.data;
            console.log(this.TakenNames);
        });
    }
}
</script>