<template>
  <div class="wish-item">
    <a :href="wish.link" class="img-box" target="_blank" rel="noopener noreferrer">
      <img :src="wish.image" alt="Wish Image" />
    </a>
    <div class="description">
      <h3>{{ wish.name }}</h3>
      <p>{{ wish.price }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    wish: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.wish-item {
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  text-align: center;
}

.wish-item:hover {
  transform: translateY(-10px);
}

.img-box {
  display: flex;
  width: 205px;
  height: 205px;
  text-align: center;
  padding: 16px;
  align-items: center;
}

.img-box img {
  max-width: 205px;
  height: auto;
  display: block;
  margin: 0 auto;
  object-fit: cover;
  border-radius: 10px;
}

.description {
  padding: 16px;
}

.description h3 {
  margin: 0;
  font-size: 1.2em;
}

.description p {
  margin: 8px 0;
}
</style>