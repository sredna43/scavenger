<template>
    <section>
        <h4>Sign up:</h4>
        <b-field label="Name">
            <b-input v-model="name"></b-input>
        </b-field>
        <b-field 
            label="Username" 
            :type=checkUser.success
            :message=checkUser.message>
            <b-input v-model="username" @input=checkUsername></b-input>
        </b-field>
        <b-field label="Password">
            <b-input type="password" password-reveal @focus="checkUsername"></b-input>
        </b-field>

    </section>
</template>

<script>
export default {
    name: "SignUpForm",
    data() {
        return {
            checkUser: {
                success: "is-success",
                message: "This username is available"
            }
        }
    },
    methods: {
        checkUsername(){
            var TakenNames = ["Test", "Apples"]
            if(!TakenNames.includes(this.username)){
                this.checkUser.success = "is-success";
                this.checkUser.message = "This username is available"
            }
            else {
                this.checkUser.success = "is-danger";
                this.checkUser.message = "Username taken";
            }
        }
    },
}
</script>