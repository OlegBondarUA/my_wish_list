<template>
  <div class="wrapper">
    <form @submit.prevent="login">
      <h1>Login</h1>
      <div class="input-box">
        <input v-model="username" type="text" placeholder="Username" required />
        <i class="bx bx-user"></i>
      </div>
      <div class="input-box">
        <input v-model="password" type="password" placeholder="Password" required />
        <i class="bx bx-lock-alt"></i>
      </div>
      <div class="remember">
        <label><input type="checkbox" v-model="rememberMe" />Remember me</label>
        <a href="#">Forgot password?</a>
      </div>
      <button type="submit" class="btn">Login</button>
      <div class="register-link">
        <p>Don’t have an account? <a href="#">Register</a></p>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      rememberMe: false,
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://localhost:8000/api/token/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          const token = data.access;

          if (this.rememberMe) {
            localStorage.setItem('access_token', token);
          } else {
            sessionStorage.setItem('access_token', token);
          }

          this.$router.push('/');

        } else {
          const errorData = await response.json();
          console.error('Login failed:', errorData);
          alert('Invalid credentials');
        }
      } catch (error) {
        console.error('Error during login:', error);
        alert('Something went wrong, please try again later.');
      }
    },
  },
};
</script>

<style scoped>

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body{
  display: flex;
  justify-content: center;
  align-content: center;
  min-height: 100vh;
}

.wrapper{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 420px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgb(255, 255, 255, .2);
  backdrop-filter: blur(20px);
  box-shadow: 0 0 10px rgba(0, 0, 0, .2);
  color: #fff;
  border-radius: 10px;
  padding: 30px 40px;
}

.wrapper h1{
  font-size: 36px;
  text-align: center;
}

.wrapper .input-box{
  width: 100%;
  height: 50px;
  margin: 30px 0;
  position: relative;
}

.input-box input{
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

.input-box input::placeholder{
  color: #fff;
}

.input-box i{
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
}

.wrapper .remember{
  display: flex;
  justify-content: space-between;
  font-size: 14.5px;
  margin: -15px 0 15px;
}

.remember label input{
  accent-color: #fff;
  margin-right: 3px;
}

.remember a{
  color: #fff;
  text-decoration: none;
}

.remember a:hover{
  text-decoration: underline;
}

.wrapper .btn{
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

.wrapper .register-link{
  font-size: 14.5px;
  text-align: center;
  margin-top: 20px;
}

.register-link p a{
  color: #fff;
  text-decoration: none;
  font-weight: 600;
}

.register-link p a:hover{
  text-decoration: underline;
  color: green;
}
</style>