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
            <b-input v-model="username" @input=checkUsername maxlength="30"></b-input>
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
//var passwordHash = require('password-hash');
export default {
    name: "SignUpForm",
    data() {
        return {
            checkUser: {
                success: "",
                message: "",
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
        }
    },
    methods: {
        checkUsername(){
            var TakenNames = ["Test", "Apples"]
            if(!TakenNames.includes(this.username) && this.username.length > 3){
                this.checkUser.success = "is-success";
                this.checkUser.message = "";
                this.checkUser.taken = false;
            }
            else {
                this.checkUser.success = "is-danger";
                this.checkUser.message = "Username taken or is too short - must be 4 characters";
                this.checkUser.taken = true;
            }
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
            this.checkUsername();
            this.checkPassword();
            if(!this.checkUser.taken && this.checkPass.valid && this.checkPass.match){
                this.$buefy.toast.open("Signed up successfully")
                // Do create user stuff on backend
                this.$router.push({name: 'NewUser', params: {user: this.name}})
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
}
</script>