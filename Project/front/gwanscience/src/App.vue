<template>
  <div id="app" class="bg-img">
    <div v-if="$router.history.current['path']!='/'">
  <b-navbar variant="faded" type="light" class="pl-0 mb-3">
      <img src="../src/assets/main_img/back.png" onclick="history.back()" class="back" align="left">
    <b-navbar-brand>
      <router-link :to="{ name: 'Home' }">
      <img src="../src/assets/main_img/logo.png" class="mini-logo">
      </router-link>
    </b-navbar-brand>
  </b-navbar>
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
  font-family: "BMEULJIRO";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/BMEULJIRO.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "BMYEONSUNG";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMYEONSUNG.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face { 
  font-family: 'Chosunilbo_myungjo'; 
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Chosunilbo_myungjo.woff') format('woff'); 
  font-weight: normal; 
  font-style: normal; 
  }


/* 을지로 폰트 */
.f-ujr {
  font-family: BMEULJIRO;
  color: black;
}

/* 연성 폰트 */
.f-ys {
  font-family: BMYEONSUNG;
  color: black;
}

/* 조선일보명조체 */
.f-cs {
  font-family: Chosunilbo_myungjo;
  color: black;
}

/* 컬러 팔레트 */
  /* 배경색 */
.bg-red{
  background-color: RGB(192, 0, 0);
  color: white;
  /* background-color: blueviolet; */
}
.bg-blue{
  background-color: RGB(46, 117, 182);
  color: white;
}
.bg-green{
  background-color: RGB(84, 130, 53);
  color: white;
}

  /* 글자색 */
.t-red{
  color: RGB(192, 0, 0);
}
.t-blue{
  color: RGB(46, 117, 182);
}
.t-green{
  color: RGB(84, 130, 53);
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

img.back {
  height: 35px;
  margin: 10px;
}


#nav a {
  font-weight: bold;
  color:black
}

#nav a.router-link-exact-active {
  color: RGB(46, 117, 182);
}

.bg-img {
  background-image: url(assets/main_img/bg.png);
  min-height: 100%;
  background-repeat: repeat-y;
  background-attachment: fixed;
  background-position: center;
  background-size: cover;
  background-color: (248, 244, 233);
  top: 0;
  left: 0;
  /* position: fixed; */
  /* Preserve aspet ratio */
  min-width: 100%;
  /* min-height: 100%; */
}

.mini-logo {
  align-content: center;
  justify-content: center;
  max-width: 50%;
  max-height: 30%;
}

</style>
