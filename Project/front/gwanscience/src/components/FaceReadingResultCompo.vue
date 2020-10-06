<template>
  <div>
    <!-- <h3 class="f-ujr">조선시대, {{ this.result.username }}님의 신분은 ?</h3> -->
    <div>결과 이미지 - 내 신분</div>
    <br>
    <br>

    <h3 class="f-ujr">나와 잘 맞는 친구는 ? </h3>
    <div>결과 이미지 - 맞는 친구</div>
    <br>
    <br>

    <h3 class="f-ujr">나와 안 맞는 친구는 ? </h3>
    <div>결과 이미지 - 안맞는 친구</div>
    <br>
    <br>
  </div>
</template>

<script>
export default {
  name: "FaceReadingResultCompo",
//   props: {
//     result: {
//       type: Object,
//     },
//   },
//   data() {
//     return {
//       my_res_url: null,
//       res1_url: null,
//       res2_url: null,
//     };
//   },
//   created() {
//     this.loadImg();
//   },
//   methods: {
//     getImgUrl(url) {
//       if (url != null) {
//         return require("../assets/" + url);
//       } else {
//         return require("../assets/clock_img/80.png");
//       }
//     },
//     loadImg() {
//       this.img_url = "../assets/" + this.result.img_url;
//       return "../assets/" + this.result.img_url;
//     },
//   },
};
</script>

<style>

</style>