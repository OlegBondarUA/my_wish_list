<template>
  <header>
    <h1>Welcome to My Wishlist</h1>
    <nav>
      <ul>
        <li><router-link to="/">Wishes</router-link></li>
        <li><router-link to="/reserved">Reserved Wishes</router-link></li>
        <li><router-link to="/achieved">Achieved Wishes</router-link></li>
        <li><router-link to="/login">Login</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f8f9fa;
}

h1 {
  margin: 0;
  font-size: 24px;
}

nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}

nav a {
  text-decoration: none;
  color: #007bff;
  font-weight: bold;
}

nav a:hover {
  color: #0056b3;
}
</style>