<template>
  <div>
    <h3 class="f-ujr" style="margin-bottom: 30px">
      조선시대, {{ this.$route.params.username }}님의 신분은 ?
    </h3>
    <b-container id="my_job">
      <img
        :src="require('../assets/job_img/' + this.$route.params.job + '.png')"
        alt="내 신분"
        class="img-size"
        style="height: 430px"
      />
    </b-container>
    <br />
    <br />

    <h3 class="f-ujr">나와 잘 맞는 친구는 ?</h3>

    <b-container id="my_job">
      <img
        :src="
          require('../assets/job_img/small/' +
            getGood(this.$route.params.job) +
            '.png')
        "
        alt="내 신분"
        class="img-size"
      />
    </b-container>
    <br />
    <br />

    <h3 class="f-ujr">나와 안 맞는 친구는 ?</h3>
    <b-container id="my_job">
      <img
        :src="
          require('../assets/job_img/small/' +
            getBad(this.$route.params.job) +
            '.png')
        "
        alt="내 신분"
        class="img-size"
      />
    </b-container>
    <br />
    <br />
    <FaceReadingResultShare />
    <hr />
    <div class="m-b300">
      <router-link :to="{ name: 'Home' }">
        <button
          class="btn-customm f-ujr mr-4 h5 text--white"
          style="width: 30%; background-color: var(--secondary); color: white"
        >
          처음으로
        </button>
      </router-link>
      <button
        class="btn-customm f-ujr bg-red h5"
        style="width: 50%"
        @click="detailreading()"
      >
        관상 상세보기
      </button>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// const URL = "https://j3c205.p.ssafy.io/api/services/face_reading/";
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
      timedelay: false,
      loadMent: "관상 분석 중 ...",
    };
  },
  props: {
    userInfo: {
      type: Object,
    },
    eyebrowShape: {
      type: String,
    },
    eyebrowInterval: {
      type: String,
    },
    eyeSize: {
      type: String,
    },
    eyeInterval: {
      type: String,
    },
    eyeTail: {
      type: String,
    },
    noseLength: {
      type: String,
    },
    noseWidth: {
      type: String,
    },
    mouthLength: {
      type: String,
    },
    mouthThickness: {
      type: String,
    },
    mouthTail: {
      type: String,
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
    this.putInfoDetail();
  },
  methods: {
    getGood(num) {
      var arr = [11, 5, 8, 7, 13, 1, 15, 3, 2, 14, 12, 0, 10, 4, 9, 6];
      return arr[num];
    },
    getBad(num) {
      var arr = [15, 14, 3, 2, 9, 7, 11, 5, 10, 4, 8, 6, 13, 12, 1, 0];
      return arr[num];
    },
    detailreading() {
      this.$router.push({
        name: "FaceReadingDetail",
        params: {
          eyebrowShape: this.result.eyebrowShape,
          eyebrowInterval: this.result.eyebrowInterval,
          eyeSize: this.result.eyeSize,
          eyeInterval: this.result.eyeInterval,
          eyeTail: this.result.eyeTail,
          noseLength: this.result.noseLength,
          noseWidth: this.result.noseWidth,
          mouthLength: this.result.mouthLength,
          mouthThickness: this.result.mouthThickness,
          mouthTail: this.result.mouthTail,
          eyebrowResult: this.result.eyebrowResult,
          eyeResult: this.result.eyeResult,
          noseResult: this.result.noseResult,
          mouthResult: this.result.mouthResult,
          job: this.result.job,
        },
      });
    },
    // test() {
    //   axios.post(URL)
    //     .then(res=> {
    //       this.result = res.data
    //       console.log(this.result)

    //     })
    //     .catch(err=> {
    //       console.log(err)
    //     })
    // },
    putInfoDetail() {
      this.result = this.$route.params;
    },
  },
};
</script>

<style scoped>
.img-size {
  max-height: 100%;
  max-width: 100%;
  background-color: white;
}
</style>
