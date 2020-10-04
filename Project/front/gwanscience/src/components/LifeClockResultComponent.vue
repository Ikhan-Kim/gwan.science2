<template>
  <div>
    <h1>Life Clock</h1>
    <h3>당신의 인생 시간은 {{ this.result.time }} 입니다.</h3>
    <img src="this.img_url" />{{ this.img_url }}
    <button @click="test()">test</button>
    <p>{{ this.result.ment }}</p>
  </div>
</template>

<script>
export default {
  name: "LifeClockResultComponent",
  props: {
    result: {
      type: Object,
    },
  },
  data() {
    return {
      time: null,
      ment: null,
      img_url: null,
    };
  },
  created() {
    this.loadImg();
  },
  methods: {
    getImgUrl(url) {
      if (url != null) {
        return require("../assets/" + url);
      } else {
        return require("../assets/clock_img/80.png");
      }
    },
    loadImg() {
      this.img_url = "../assets/" + this.result.img_url;
      return "../assets/" + this.result.img_url;
    },
    test() {
      console.log(
        this.result.time,
        this.result.ment,
        this.result.img_url,
        this.img_url
      );
    },
  },
};
</script>

<style>
</style>