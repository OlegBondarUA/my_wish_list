<template>
  <div>
    <h1>My Wishes</h1>
    <div v-if="wishes.length">
      <WishItem v-for="wish in wishes" :key="wish.id" :wish="wish" />
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

div {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>