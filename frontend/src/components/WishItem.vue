<template>
  <div class="wish-item">
    <img :src="wish.image" alt="Wish Image" />
    <h3>{{ wish.name }}</h3>
    <p>{{ wish.link }}</p>
    <p>{{ wish.price }}</p>
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
  border: 1px solid #ccc;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 8px;
  text-align: center;
}

img {
  max-width: 100%;
  height: auto;
}
</style>