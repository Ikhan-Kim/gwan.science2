<template>
  <div>
    <h1>{{ this.result.username }}님의 관상 분석 결과</h1>
    <hr />
    <div style="width: 500px; margin: auto">
      <!-- <img :src="userInfo.userPhoto" /> -->
      <h2 style="font-family: 궁서; font-weight: bold; margin-top: 30px">
        왕의 상
      </h2>
      <p>용맹스럽고 위엄이 있으며 먹고 사는데 큰 지장이 없다.</p>
      <h3 style="margin-top: 30px">눈썹, 미간</h3>
      <h5>{{ this.result.eyebrowShape }}, {{ this.result.eeybrowInterval }}</h5>
      <p>
        {{ this.result.eyebrowResult }}
      </p>
      <h3 style="margin-top: 30px">눈</h3>
      <h5>
        {{ this.result.eyeSize }}, {{ this.result.eyeTail }},
        {{ this.result.eyeInterval }}
      </h5>
      <p>
        {{ this.result.eyeResult }}
      </p>
      <h3 style="margin-top: 30px">코</h3>
      <h5>{{ this.result.noseLength }}, {{ this.result.noseWidth }}</h5>
      <p>
        {{ this.result.noseResult }}
      </p>
      <h3 style="margin-top: 30px">입</h3>
      <h5>
        {{ this.result.mouthLength }}, {{ this.result.mouthThickness }},
        {{ this.result.mouthTail }}
      </h5>
      <p>{{ this.result.mouthResult }}</p>
    </div>
    <FaceReadingResultShare style="margin: 50px" />
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
