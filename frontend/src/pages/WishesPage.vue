<template>
  <div>
    <h1>My Wishes</h1>
    <div v-if="wishes.length">
      <div class="wish-list">
        <WishItem v-for="wish in wishes" :key="wish.id" :wish="wish" />
      </div>
    </div>
    <div v-else>
      <p>No wishes found.</p>
    </div>
  </div>
</template>

<script>
import WishItem from '../components/WishItem.vue';

export default {
  components: {
    WishItem
  },
  data() {
    return {
      wishes: []
    };
  },
  mounted() {
    this.fetchWishes();
  },
  methods: {
    async fetchWishes() {
      try {
        const response = await fetch('http://localhost:8000/api/wishes/');
        this.wishes = await response.json();
      } catch (error) {
        console.error('Failed to fetch wishes:', error);
      }
    }
  }
}
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 24px;
}

.wish-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
  padding: 0 16px;
}

@media (max-width: 600px) {
  .wish-list {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>