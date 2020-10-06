<template>
  <div>
    <h3 class="f-ujr">조선시대, {{ this.result.username }}님의 신분은 ?</h3>
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
    <FaceReadingResultShare />
    <hr>
    <div class="m-b300">
      <router-link :to="{ name: 'Home' }">
      <button class="btn-customm f-ujr mr-4 h5 text--white" style="width: 30%;  background-color: var(--secondary); color: white;" @click="takePhoto">처음으로</button>
      </router-link>

      <router-link :to="{ name: 'FaceReadingDetail' }">
      <button class="btn-customm f-ujr bg-red h5" style="width: 50%">관상 상세보기</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const URL = "http://127.0.0.1:8000/services/face_reading/";
import FaceReadingResultShare from "@/components/FaceReadingResultShare.vue";

export default {
  name: "FaceReadingResult",
  data() {
    return {
      result: {
        username: null,
        eyebrowShape: null,
        eyebrowInterval: null,
        eyeSize: null,
        eyeInterval: null,
        eyeTail: null,
        noseLength: null,
        noseWidth: null,
        mouthLength: null,
        mouthThickness: null,
        mouthTail: null,
        eyebrowResult: null,
        eyeResult: null,
        noseResult: null,
        mouthResult: null,
        totalResult: null,
      },
    };
  },
  props: {
    userInfo: {
      type: Object,
    },
  },
  metaInfo: {},
  components: {
    FaceReadingResultShare,
  },
  created() {
    // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.
    if (!window.Kakao.isInitialized()) {
      window.Kakao.init("461657f0b2d7529bbc498714486b6b12");
    }
    // SDK 초기화 여부를 판단합니다.
    console.log(window.Kakao.isInitialized());
    axios.get(URL + "test").then((res) => {
      this.result = res.data;
      console.log(this.result);
    });
  },
};
</script>

<style scoped></style>
