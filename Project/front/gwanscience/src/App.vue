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
  /* position: fixed; */
  /* background-attachment: fixed; */
  top: 0; 
  left: 0; 
  overflow-y:auto;
  overflow-x:scroll;

  /* Preserve aspet ratio */
  min-width: 100%;
  min-height: 100%;
}

.m-b300 {
  margin-bottom: 300px;
}
</style>
