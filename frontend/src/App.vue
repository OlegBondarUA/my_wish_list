<script setup>
import Header from './components/Header.vue'
import WishesPage from './pages/WishesPage.vue'
</script>

<template>
  <Header />
  <router-view />
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>