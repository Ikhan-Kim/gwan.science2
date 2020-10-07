<template>
  <div>
    <b-container>
      <b-row class="f-ujr" v-if="this.timedelay">
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle1.png" width="100%" />
            <div class="example">
              <p>{{ this.result.name[0][0] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle2.png" width="100%" />
            <div class="example">
              <p>{{ this.result.name[1][0] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle3.png" width="100%" />
            <div class="example">
              <p>{{ this.result.name[0][1] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle4.png" width="100%" />
            <div class="example">
              <p>{{ this.result.name[1][1] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle5.png" width="100%" />
            <div class="example">
              <p>{{ this.result.name[0][2] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="2">
          <div>
            <img src="@/assets/name_img/circle6.png" width="100%" />
            <div class="example" style="width: 100%">
              <p>{{ this.result.name[1][2] }}</p>
            </div>
          </div>
        </b-col>
        <b-col cols="12">
          <div>
            <img src="@/assets/name_img/cal.png" width="100%" />
            <div class="cexample" style="top: 11%; left: 12%">
              {{ this.result.cal[0][0][0] }}
            </div>
            <div class="cexample" style="top: 11%; left: 27%">
              {{ this.result.cal[0][0][1] }}
            </div>
            <div class="cexample" style="top: 11%; left: 42%">
              {{ this.result.cal[0][0][2] }}
            </div>
            <div class="cexample" style="top: 11%; left: 58%">
              {{ this.result.cal[0][0][3] }}
            </div>
            <div class="cexample" style="top: 11%; left: 74%">
              {{ this.result.cal[0][0][4] }}
            </div>
            <div class="cexample" style="top: 11%; left: 89%">
              {{ this.result.cal[0][0][5] }}
            </div>
            <div class="cexample" style="top: 33%; left: 19%">
              {{ this.result.cal[0][1][0] }}
            </div>
            <div class="cexample" style="top: 33%; left: 34%">
              {{ this.result.cal[0][1][1] }}
            </div>
            <div class="cexample" style="top: 33%; left: 49%">
              {{ this.result.cal[0][1][2] }}
            </div>
            <div class="cexample" style="top: 33%; left: 66%">
              {{ this.result.cal[0][1][3] }}
            </div>
            <div class="cexample" style="top: 33%; left: 81%">
              {{ this.result.cal[0][1][4] }}
            </div>
            <div class="cexample" style="top: 52%; left: 27%">
              {{ this.result.cal[0][2][0] }}
            </div>
            <div class="cexample" style="top: 52%; left: 42%">
              {{ this.result.cal[0][2][1] }}
            </div>
            <div class="cexample" style="top: 52%; left: 57%">
              {{ this.result.cal[0][2][2] }}
            </div>
            <div class="cexample" style="top: 52%; left: 73%">
              {{ this.result.cal[0][2][3] }}
            </div>
            <div class="cexample" style="top: 70%; left: 34%">
              {{ this.result.cal[0][3][0] }}
            </div>
            <div class="cexample" style="top: 70%; left: 50%">
              {{ this.result.cal[0][3][1] }}
            </div>
            <div class="cexample" style="top: 70%; left: 66%">
              {{ this.result.cal[0][3][2] }}
            </div>
            <div class="cexample" style="top: 88%; left: 41%">
              {{ this.result.cal[0][4][0] }}
            </div>
            <div class="cexample" style="top: 88%; left: 58%">
              {{ this.result.cal[0][4][1] }}
            </div>
          </div>
        </b-col>
      </b-row>
      <spinner :loading="this.timedelay" :loadingMent="this.loadMent"></spinner>
      <h5 class="f-ujr" style="margin-top: 20px">
        {{ this.result.name[0] }}님은 {{ this.result.name[1] }}님과의
      </h5>
      <h5 class="f-ujr">궁합은 {{ this.result.score[0] }}% 입니다.</h5>
      <h4 class="f-ujr" style="color: red; margin-top: 30px">
        " {{ this.result.comment }} "
      </h4>
    </b-container>
    <NameCompatibilityResultShare />
  </div>
</template>

<script>
import NameCompatibilityResultShare from "@/components/NameCompatibilityResultShare.vue";
import spinner from "@/components/spinner.vue";
import axios from "axios";

const URL = "https://j3c205.p.ssafy.io/api/services/name_compability/";

export default {
  name: "NameCompatibilityResult",
  metaInfo: {},
  data() {
    return {
      result: {
        name: [null, null],
        score: [null, null],
        cal: [null, null],
        comment: null,
      },
      timedelay: false,
      loadMent: "이름 궁합 계산중...",
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
    spinner,
  },
  created() {
    // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.
    if (!window.Kakao.isInitialized()) {
      window.Kakao.init("461657f0b2d7529bbc498714486b6b12");
    }
    // SDK 초기화 여부를 판단합니다.
    console.log(window.Kakao.isInitialized());

    this.loadresult();
    setTimeout(() => {
      this.timeout();
    }, 1500);
  },
  methods: {
    loadresult() {
      axios
        .get(URL + this.$route.params.name1 + "/" + this.$route.params.name2)
        .then((res) => {
          this.result = res.data;
          console.log(res.data);
        });
    },
    timeout() {
      this.timedelay = true;
    },
  },
};
</script>

<style scoped>
.name-img {
  width: 100%;
  vertical-align: middle;
}
.name-text {
  padding: 5px 10px;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

@media screen and (min-width: 768px) {
  div.example {
    font-size: 25px;
    text-align: center;
    position: absolute;
    top: 63%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

@media screen and (max-width: 768px) {
  div.example {
    font-size: 20px;
    text-align: center;
    position: absolute;
    top: 63%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

@media screen and (max-width: 376px) {
  div.example {
    font-size: 14px;
    text-align: center;
    position: absolute;
    top: 77%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

@media screen and (min-width: 768px) {
  div.cexample {
    font-size: 25px;
    text-align: center;
    position: absolute;
    transform: translate(-50%, -50%);
  }
}

@media screen and (max-width: 768px) {
  div.cexample {
    font-size: 20px;
    text-align: center;
    position: absolute;
    transform: translate(-50%, -50%);
  }
}

@media screen and (max-width: 376px) {
  div.cexample {
    font-size: 14px;
    text-align: center;
    position: absolute;
    top: 63%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}
</style>
