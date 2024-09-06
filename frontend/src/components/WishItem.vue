<template>
  <div class="wish-item">
    <a :href="wish.link" class="img-box" target="_blank" rel="noopener noreferrer">
      <img :src="wish.image" alt="Wish Image" />
      <div class="overlay">
        <h3>{{ wish.name }}</h3>
      </div>
    </a>
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
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px #0000001a;
  transition: transform .3s ease;
  text-align: center;
  display: flex;
  justify-content: center;
}

.wish-item:hover {
  transform: translateY(-10px);
}

.img-box {
  position: relative;
  display: flex;
  width: 205px;
  height: 205px;
  align-items: center;
  justify-content: center;
}

.img-box img {
  max-width: 205px;
  height: auto;
  object-fit: cover;
  border-radius: 10px;
  transition: opacity 0.3s ease;
}

.img-box .overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.img-box:hover .overlay {
  opacity: 1;
}

.overlay h3 {
  color: white;
  font-size: 1.5em;
  text-align: center;
}
</style>
