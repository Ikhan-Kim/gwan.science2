<template>
  <div>
    <h3 class="f-ujr">당신의 인생 시간은 <br>
    {{ this.result.time }} 입니다.</h3>
    <img class="clock-size" :src="getImgUrl(this.result.img_url)" />
    <p class="f-cs">{{ this.result.ment }}</p>
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
  },
};
</script>

<style>
.clock-size {
  max-width: 80%;
  max-height: 70%;
}
</style>
