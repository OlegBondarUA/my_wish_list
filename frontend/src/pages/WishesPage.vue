<template>
  <div>
    <h1>Wishes</h1>

    <div v-if="wishes.length">
      <div class="wish-list">
        <WishItem v-for="wish in wishes" :key="wish.id" :wish="wish" />
        <div class="add-wish-card" @click="toggleForm">
          <span>+</span>
        </div>
      </div>
    </div>

    <div v-else>
      <p>No wishes found.</p>
    </div>

    <div v-if="showForm" class="wish-form">
      <h2>Add New Wish</h2>
      <form @submit.prevent="submitForm">
        <label for="name">Name:</label>
        <input type="text" v-model="newWish.name" required />

        <label for="image">Image:</label>
        <input type="file" @change="handleFileUpload" required />

        <label for="description">Description:</label>
        <textarea v-model="newWish.description"></textarea>

        <label for="link">Link:</label>
        <input type="url" v-model="newWish.link" required />

        <label for="price">Price:</label>
        <input type="number" v-model="newWish.price" step="0.01" required />
        <div class="button-box">
          <button type="submit">Add Wish</button>
          <button type="button" @click="toggleForm">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import WishItem from '../components/WishItem.vue';

export default {
  components: {
    WishItem,
  },
  data() {
    return {
      wishes: [],
      showForm: false, // Додаємо стан для показу форми
      newWish: {
        name: '',
        image: null,
        description: '',
        link: '',
        price: null,
      },
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
    },
    toggleForm() {
      this.showForm = !this.showForm;
    },
    handleFileUpload(event) {
      this.newWish.image = event.target.files[0];
    },
    submitForm() {
      console.log(this.newWish); // Логіка для відправлення нового бажання
      this.toggleForm(); // Закриваємо форму після додавання
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 24px;
  color: white;
  font-family: "Playwrite CU", cursive;
  font-optical-sizing: auto;
}

.wish-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 16px;
  padding: 0 20px;
}

.add-wish-card {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px dashed #ccc;
  border-radius: 10px;
  cursor: pointer;
  font-size: 2em;
  color: white;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

.wish-form {
  max-width: 275px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
  justify-content: center;
  background: ghostwhite;
  padding: 20px;
  border-radius: 15px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
}

.wish-form form {
  width: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-direction: column;
}
.wish-form label {
  font-weight: bold;
}

.wish-form input,
.wish-form textarea {
  width: 255px;
  height: 20px;
  padding: 8px;
  border: 2px solid darkseagreen;
  border-radius: 10px;
}

.button-box {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

button {
  padding: 10px;
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button[type="button"] {
  background-color: #6c757d;
}

button:hover {
  background-color: #0056b3;
}

@media (max-width: 600px) {
  .wish-list {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>>