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
  padding: 0 10px;
  border-radius: 0 0 15px 15px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

h1 {
  margin: 0;
  font-size: 28px;
  font-family: "Playwrite CU", cursive;
  font-optical-sizing: auto;
  color: #fff;
}

nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
}

nav a {
  text-decoration: none;
  color: #ffffff;
  font-family: "Playwrite CU", cursive;
  font-optical-sizing: auto;
  font-weight: bold;
  font-size: 18px;
  transition: color 0.3s ease;
}

nav a:hover {
  color: #50c878;
}
</style>
