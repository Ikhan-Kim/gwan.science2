<template>
  <div>
    <hr />
    <h3>{{ name1 }}님의 {{ name2 }}님을 생각하는 호감도 {{ score1 }}%</h3>
    <h3>{{ name2 }}님의 {{ name1 }}님을 생각하는 호감도 {{ score2 }}%</h3>
    <div style="width: 500px; margin: auto"></div>
    <NameCompatibilityResultShare style="margin: 50px" />
  </div>
</template>

<script>
import NameCompatibilityResultShare from "@/components/NameCompatibilityResultShare.vue";
import axios from "axios";

const test_URL = "http://127.0.0.1:8000/services/name_compability/";

export default {
  name: "FaceReadingResult",
  metaInfo: {},
  data() {
    return {
      score1: 0,
      score2: 0,
    };
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

    const nameData = {
      name1: this.name1,
      name2: this.name2,
    };
    axios.post(test_URL, nameData).then((res) => {
      if (res.status === 200) {
        console.log(res);
        this.score1 = res.data.jumsu1;
        this.score2 = res.data.jumsu2;
      }
    });
  },
};
</script>

<style scoped></style>
