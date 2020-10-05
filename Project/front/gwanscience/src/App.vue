<template>
  <div id="app" class="bg-img">
    <div id="nav">
      <router-link to="/">홈</router-link>|
      <router-link to="/FaceReading">관상</router-link>|
      <router-link to="/NameCompatibility">이름 궁합</router-link>|
      <router-link to="/LifeClock">인생 시계</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "app",
};
</script>

<style>
@font-face { 
  font-family: 'BMEULJIRO'; 
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/BMEULJIRO.woff') format('woff'); 
  font-weight: normal; 
  font-style: normal; }

@font-face { 
  font-family: 'BMYEONSUNG'; 
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMYEONSUNG.woff') format('woff'); 
  font-weight: normal; 
  font-style: normal; }

/* 을지로 폰트 */
.f-ujr { 
  font-family: BMEULJIRO;
}

/* 연성 폰트 */
.f-ys {
  font-family: BMYEONSUNG;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.bg-img {
  background-image: url(assets/main_img/bg.png);
  background-color: (248, 244, 233);
  position: fixed; 
  top: 0; 
  left: 0; 

  /* Preserve aspet ratio */
  min-width: 100%;
  min-height: 100%;
}
</style>
