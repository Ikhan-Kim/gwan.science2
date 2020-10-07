<template>
  <div>
    {{ this.$route.params }}
    <h3 class="f-ujr mb-5">관상 상세 분석 결과</h3>
    <!-- 탭 방식 -->
    <b-tabs card justified content-class="mt-2 mb-5" class="f-ujr">
    <b-tab title="눈썹" class="content-box" active>
      <p class="f-ys h5 pb-3">"{{ this.result.eyebrowShape }}"을 가진 당신은,</p>
      <p class="f-cs">활발한 말괄량이 타입으로 해석. 간혹 성격이 급하고 욱하는 경향이 있어 주변 사람들을 당황스럽게 할 때도 있다고 함.</p>
    </b-tab>
    <b-tab title="눈" class="content-box">
      <p class="f-ys h5 pb-3">"진하고 위로 올라간 눈썹"을 가진 당신은,</p>
      <p class="f-cs">활발한 말괄량이 타입으로 해석. 간혹 성격이 급하고 욱하는 경향이 있어 주변 사람들을 당황스럽게 할 때도 있다고 함.</p>
    </b-tab>
    <b-tab title="코" class="content-box">
      <p class="f-ys h5 pb-3">"진하고 위로 올라간 눈썹"을 가진 당신은,</p>
      <p class="f-cs">활발한 말괄량이 타입으로 해석. 간혹 성격이 급하고 욱하는 경향이 있어 주변 사람들을 당황스럽게 할 때도 있다고 함.</p>
    </b-tab>
    <b-tab title="입" class="content-box">
      <p class="f-ys h5 pb-3">"진하고 위로 올라간 눈썹"을 가진 당신은,</p>
      <p class="f-cs">활발한 말괄량이 타입으로 해석. 간혹 성격이 급하고 욱하는 경향이 있어 주변 사람들을 당황스럽게 할 때도 있다고 함.</p>
    </b-tab>
  </b-tabs>
  

  <router-link :to="{ name: 'Home' }">
    <button class="btn-customm f-ujr mr-4 h5 text--white bg-red" style="width: 30%;">처음으로</button>
  </router-link>


  </div>
</template>

<script>
import axios from "axios";
const URL = "http://127.0.0.1:8000/services/face_reading/";

export default {
  name: "FaceReadingDetail",
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
        job: null,
      },
      timedelay: false,
      loadMent: '관상 분석 중 ...'
    };
  },
  created() {
    axios.post(URL).then((res) => {
      this.result = res.data;
      console.log('resultDetail:',this.result);
    });
  }
}
</script>

<style scoped>
.content-box {
  width: 100%;
  max-height: 80%;
  background-color: white;
  color: black;
  text-align: start;
}
</style>

