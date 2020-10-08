<template>
  <div>
    <h5 class="f-ujr" style="width: 80%; margin-left: 10%">당신의 나이는 {{ this.$route.params.age }}살입니다.<br>
      이 나이를 하루 24시간으로 환산하면 <br>
    </h5>
    <h5 class="f-ujr" style="color: red">  {{ this.result.time }} 입니다.</h5>
    <br>
    <img class="clock-size" :src="getImgUrl(this.result.img_url)"/>
    <br>
    <h5 class="f-ujr" style="width: 80%; margin-bottom: 70px; margin-left: 10%; margin-top: 30px; font-weight: lighter">
      {{ this.result.ment }}</h5>
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
