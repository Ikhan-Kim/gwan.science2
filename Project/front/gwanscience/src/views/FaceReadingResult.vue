<template>
  <div>
    <h3 class="f-ujr">조선시대, {{ this.result.username }}님의 신분은 ?</h3>
    <b-container id="my_job">
      <img src="../assets/job_img/1.png" alt="내 신분" class="img-size">
<!--      <img :src="require('../assets/job_img/'+result.job+'.png')" alt="내 신분" class="img-size">-->
    </b-container>
    <br>
    <br>

    <h3 class="f-ujr">나와 잘 맞는 친구는 ? </h3>

    <!-- <b-button v-b-toggle.collapse-3 class="m-1">Toggle Collapse</b-button>
  <b-collapse visible id="collapse-3">
    <b-card>I should start open!</b-card>
  </b-collapse> -->

    <b-container id="my_job">
        <img :src="require('../assets/job_img/small/'+getGood(1)+'.png')" alt="내 신분" class="img-size">
    </b-container>
    <br>
    <br>

    <h3 class="f-ujr">나와 안 맞는 친구는 ? </h3>
    <b-container id="my_job">
      <img :src="require('../assets/job_img/small/'+getBad(1)+'.png')" alt="내 신분" class="img-size">
    </b-container>
    <br>
    <br>
    <FaceReadingResultShare/>
    <hr>
    <div class="m-b300">
      <router-link :to="{ name: 'Home' }">
        <button class="btn-customm f-ujr mr-4 h5 text--white"
                style="width: 30%;  background-color: var(--secondary); color: white;">처음으로
        </button>
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
        job: null,
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
  methods: {
    getGood(num) {
      var arr = [11, 5, 8, 7, 13, 1, 15, 3, 2, 14, 12, 0, 10, 4, 9, 6];
      return arr[num];
    },
    getBad(num) {
      var arr = [15, 14, 3, 2, 9, 7, 11, 5, 10, 4, 8, 6, 13, 12, 1, 0];
      return arr[num];
    }
  }

};
</script>

<style scoped>
.img-size {
  max-height: 100%;
  max-width: 100%;
  background-color: white;
}
</style>
