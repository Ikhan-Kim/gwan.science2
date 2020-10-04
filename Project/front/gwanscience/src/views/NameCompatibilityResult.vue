<template>
  <div>
    <hr />
    <h3>{{ this.result.name[0] }}님의 {{ this.result.name[1] }}님을 생각하는 호감도 {{ this.result.score[0] }}%</h3>
    <h3>{{ this.result.name[1] }}님의 {{ this.result.name[0] }}님을 생각하는 호감도 {{ this.result.score[1] }}%</h3>
    <div style="width: 500px; margin: auto"></div>
    <NameCompatibilityResultShare style="margin: 50px" />
  </div>
</template>

<script>
import NameCompatibilityResultShare from "@/components/NameCompatibilityResultShare.vue";
import axios from "axios";

const URL = "http://127.0.0.1:8000/services/test/"

export default {
  name: "NameCompatibilityResult",
  metaInfo: {},
  data () {
    return {
      result: {
        name: [null, null],
        score: [null, null],
      }
    }
  },
  props: {
    name1: {
      type: String,
    },
    name2: {
      type: String,
    },
  },
  components: {
    NameCompatibilityResultShare,
  },
  created() {
    // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.
    if (!window.Kakao.isInitialized()) {
      window.Kakao.init("461657f0b2d7529bbc498714486b6b12");
    }
    // SDK 초기화 여부를 판단합니다.
    console.log(window.Kakao.isInitialized());

    this.loadresult();
  },
  methods: {
    loadresult() {
      axios.get(URL + this.$route.params.name1 + '/' + this.$route.params.name2)
      .then(res => {
        this.result = res.data
      })
    }
  }
};
</script>

<style scoped></style>
