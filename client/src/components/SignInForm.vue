<template>
    <div>
        <h4>Sign in:</h4>
        <b-field 
            label="Username">
            <b-input v-model="username"></b-input>
        </b-field>
        <b-field label="Password">
            <b-input type="password" password-reveal></b-input>
        </b-field>
        
            <div class="buttons is-right">
                <b-button class="submit button is-secondary" @click.native="clearForm">Cancel</b-button>
                <b-button class="submit button is-primary" @click.native="submitForm">Login</b-button>
            </div>
        
    </div>
</template>

<script>
export default {
    name: "SignInForm"
}
</script>

<style scoped>

</style>