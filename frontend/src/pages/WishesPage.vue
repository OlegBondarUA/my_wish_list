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

    <div v-if="showForm" class="wrapper">
      <form @submit.prevent="submitForm">
        <h1>Add New Wish</h1>
        <div class="input-box">
          <input type="text" v-model="newWish.title" placeholder="Title" required/>
          <i class='bx bx-captions'></i>
        </div>

        <div class="input-box">
          <input type="file" id="file-input" @change="handleFileChange" required/>
          <label for="file-input" class="file-label">
            <span id="file-name">No file chosen</span>
            <i class='bx bx-image-add'></i>
          </label>
        </div>

        <div class="input-box">
          <input type="text" v-model="newWish.description" placeholder="Description" required/>
          <i class='bx bx-detail'></i>
        </div>

        <div class="input-box">
          <input type="url" v-model="newWish.link" placeholder="link" required/>
          <i class='bx bx-link'></i>
        </div>

        <div class="input-box">
          <input type="number" v-model="newWish.price" placeholder="Price" required/>
          <i class='bx bx-dollar'></i>
        </div>

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
      showForm: false,
      newWish: {
        title: '',
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
    getToken() {
      return localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
    },

    getRefreshToken() {
      return localStorage.getItem('refresh_token') || sessionStorage.getItem('refresh_token');
    },

    async refreshAccessToken() {
      try {
        const refreshToken = this.getRefreshToken();
        const response = await fetch('http://localhost:8000/api/token/refresh/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ refresh: refreshToken }),
        });

        if (response.ok) {
          const data = await response.json();
          localStorage.setItem('access_token', data.access);
          return data.access;
        } else {
          console.error('Failed to refresh token:', await response.json());
        }
      } catch (error) {
        console.error('Error refreshing token:', error);
      }
    },

    async fetchWishes() {
      try {
        let token = this.getToken();
        if (!token) {
          throw new Error('User is not authenticated');
        }

        let response = await fetch('http://localhost:8000/api/wishes/', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (response.status === 401) {
          const errorData = await response.json();
          if (errorData.code === 'token_not_valid') {
            token = await this.refreshAccessToken();
            if (token) {
              response = await fetch('http://localhost:8000/api/wishes/', {
                method: 'GET',
                headers: {
                  'Authorization': `Bearer ${token}`,
                },
              });
            }
          }
        }

        if (response.ok) {
          this.wishes = await response.json();
        } else {
          console.error('Failed to fetch wishes:', await response.json());
        }
      } catch (error) {
        console.error('Failed to fetch wishes:', error);
      }
    },

    toggleForm() {
      this.showForm = !this.showForm;
    },

    handleFileChange(event) {
      const fileInput = event.target;
      document.getElementById('file-name').textContent = fileInput.files[0] ? fileInput.files[0].name : 'No file chosen';
      this.newWish.image = fileInput.files[0];
    },

    async submitForm() {
      const formData = new FormData();
      formData.append('title', this.newWish.title);
      formData.append('image', this.newWish.image);
      formData.append('description', this.newWish.description);
      formData.append('link', this.newWish.link);
      formData.append('price', this.newWish.price);

      try {
        let token = this.getToken();
        if (!token) {
          throw new Error('User is not authenticated');
        }

        let response = await fetch('http://localhost:8000/api/wishes/add/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
          body: formData,
        });

        if (response.status === 401) {
          const errorData = await response.json();
          if (errorData.code === 'token_not_valid') {
            token = await this.refreshAccessToken();
            if (token) {
              response = await fetch('http://localhost:8000/api/wishes/add/', {
                method: 'POST',
                headers: {
                  'Authorization': `Bearer ${token}`,
                },
                body: formData,
              });
            }
          }
        }

        if (response.ok) {
          console.log('Wish added successfully');
          this.toggleForm();
          await this.fetchWishes();
        } else {
          console.error('Failed to add wish:', await response.json());
        }
      } catch (error) {
        console.error('Error adding wish:', error);
      }
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

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  display: flex;
  justify-content: center;
  align-content: center;
  min-height: 100vh;
}

.wrapper {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 420px;
  background: #1a1a1a;
  border: 2px solid rgb(255, 255, 255, .2);
  backdrop-filter: blur(20px);
  box-shadow: 0 0 10px rgba(0, 0, 0, .2);
  color: #fff;
  border-radius: 10px;
  padding: 30px 40px;
}

.wrapper h1 {
  font-size: 36px;
  text-align: center;
}

.wrapper .input-box {
  width: 100%;
  height: 50px;
  margin: 30px 0;
  position: relative;
}

.input-box input,
.input-box textarea {
  width: 100%;
  height: 100%;
  background: transparent;
  outline: none;
  border: 2px solid rgb(225, 225, 225, .2);
  border-radius: 40px;
  font-size: 16px;
  color: #fff;
  padding: 20px 45px 20px 20px;
}

.input-box input::placeholder,
.input-box textarea::placeholder {
  color: #fff;
}

.input-box i {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
}

.wrapper .button-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.wrapper .button-box button {
  width: 100%;
  height: 45px;
  background: #fff;
  border: none;
  outline: none;
  border-radius: 40px;
  box-shadow: 0 0 10px rgb(0, 0, 0, .1);
  cursor: pointer;
  font-size: 16px;
  color: #333;
  font-weight: 600;
}

.input-box input[type="file"] {
  display: none;
}

.file-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  background: transparent;
  outline: none;
  border: 2px solid rgb(225, 225, 225, .2);
  border-radius: 40px;
  font-size: 16px;
  color: #fff;
  padding: 20px 45px 20px 20px;
  cursor: pointer;
}

.file-label span {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 600px) {
  .wish-list {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>