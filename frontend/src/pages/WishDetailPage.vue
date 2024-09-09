<template>
  <div class="wish-detail">
    <img :src="wish.image" alt="Wish Image" class="wish-image" />
    <h1>{{ wish.name }}</h1>
    <p>{{ wish.description }}</p>
    <p><strong>Price:</strong> {{ wish.price }}</p>

    <div class="wish-actions">
      <button @click="reserveWish" :disabled="wish.reserved">
        {{ wish.reserved ? 'Reserved' : 'Reserve' }}
      </button>
      <a :href="wish.link" target="_blank" class="go-to-store">
        Go to store
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      wish: null,
    };
  },
  mounted() {
    this.fetchWishDetail();
  },
  methods: {
    async fetchWishDetail() {
      try {
        const response = await fetch(`http://localhost:8000/api/wishes/${this.$route.params.id}/`);
        this.wish = await response.json();
      } catch (error) {
        console.error('Error fetching wish detail:', error);
      }
    },
    async reserveWish() {
      try {
        const response = await fetch(`http://localhost:8000/api/wishes/${this.wish.id}/reserve/`, {
          method: 'POST',
        });
        if (response.ok) {
          this.wish.reserved = true;
        }
      } catch (error) {
        console.error('Error reserving wish:', error);
      }
    }
  }
};
</script>

<style scoped>
.wish-detail {
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.wish-image {
  max-width: 100%;
  border-radius: 10px;
  margin-bottom: 20px;
}

.wish-actions {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}

button[disabled] {
  background-color: #ccc;
}

.go-to-store {
  padding: 10px 20px;
  background-color: #2196f3;
  color: white;
  text-decoration: none;
  display: inline-block;
}
</style>
