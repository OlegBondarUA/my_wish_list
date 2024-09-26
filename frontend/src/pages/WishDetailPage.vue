<template>
  <div v-if="wish" class="wish-detail">
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

  <div v-else>
    Loading wish details...
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

    async fetchWishDetail() {
      try {
        let token = this.getToken();
        if (!token) {
          throw new Error('User is not authenticated');
        }

        let response = await fetch(`http://localhost:8000/api/wishes/${this.$route.params.id}/`, {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (response.status === 401) {
          const errorData = await response.json();
          if (errorData.code === 'token_not_valid') {
            token = await this.refreshAccessToken();
            if (token) {
              response = await fetch(`http://localhost:8000/api/wishes/${this.$route.params.id}/`, {
                headers: {
                  'Authorization': `Bearer ${token}`,
                },
              });
            }
          }
        }

        if (response.ok) {
          this.wish = await response.json();
        } else {
          console.error('Error fetching wish detail:', await response.json());
        }
      } catch (error) {
        console.error('Error fetching wish detail:', error);
      }
    },

    async reserveWish() {
      try {
        let token = this.getToken();
        if (!token) {
          throw new Error('User is not authenticated');
        }

        let response = await fetch(`http://localhost:8000/api/wishes/${this.wish.id}/reserve/`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (response.status === 401) {
          const errorData = await response.json();
          if (errorData.code === 'token_not_valid') {
            token = await this.refreshAccessToken();
            if (token) {
              response = await fetch(`http://localhost:8000/api/wishes/${this.wish.id}/reserve/`, {
                method: 'POST',
                headers: {
                  'Authorization': `Bearer ${token}`,
                },
              });
            }
          }
        }

        if (response.ok) {
          this.wish.reserved = true;
        } else {
          console.error('Error reserving wish:', await response.json());
        }
      } catch (error) {
        console.error('Error reserving wish:', error);
      }
    },
  },
};
</script>


<style scoped>
.wish-detail {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  background-color: #1f1f1f;
  color: #fff;
  padding: 20px;
  border-radius: 8px;
}

.wish-image {
  max-width: 300px;
  border-radius: 8px;
}

.wish-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #ff8c00;
  color: white;
  cursor: pointer;
}

button[disabled] {
  background-color: #ccc;
}

.go-to-store {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  display: inline-block;
  border-radius: 4px;
}
</style>
