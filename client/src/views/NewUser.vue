<template>
    <div>
        <h1 class="title">Welcome, {{user}}</h1>
    </div>
</template>

<script>
export default {
    name: 'NewUser',
    data() {
        return{
            user: this.$route.params.user,
        }
    },
}
</script>