<template>
  <div class="wish-item">
    <router-link :to="`/wish/${wish.id}`" class="img-box">
      <img :src="wish.image" alt="Wish Image" />
      <div class="wish-overlay">
        <h3>{{ wish.name }}</h3>
      </div>
    </router-link>
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
  display: grid;
  align-content: center;
  position: relative;
  width: 100%;
  overflow: hidden;
  border-radius: 15px;
  background: grey;
}

.img-box {
  display: block;
  position: relative;
}

.img-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 15px;
}

.wish-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.wish-item:hover .wish-overlay {
  opacity: 1;
  border-radius: 15px;
}

.wish-overlay h3 {
  color: white;
  font-size: 1.5em;
  text-align: center;
}
</style>
