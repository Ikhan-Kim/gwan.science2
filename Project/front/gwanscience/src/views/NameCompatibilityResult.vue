<template>
  <b-container>
    <!-- <div style="position: relative;">  일일이 위치지정
      <img src="@/assets/all.jpg" height="80">
      <div style="left: -80px; width: 450px; bottom: 10px; font-size: 2em; position: absolute;">
        {{ this.result.name[0][0] }}
      </div>
      <div style="left: -4px; width: 450px; bottom: 10px; font-size: 2em; position: absolute;">
        {{ this.result.name[1][0] }}
      </div>
    </div>
  <div> -->
    <hr />
    <b-row class="f-ujr">
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle1.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[0][0] }}</p>
          </div>
        </div>
      </b-col>
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle2.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[1][0] }}</p>
          </div>
        </div>
      </b-col>
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle3.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[0][1] }}</p>
          </div>
        </div>
      </b-col>
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle4.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[1][1] }}</p>
          </div>
        </div>
      </b-col>
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle5.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[0][2] }}</p>
          </div>
        </div>
      </b-col>
      <b-col cols="12" xs="2" sm="2">
        <div>
          <img src="@/assets/name_img/circle6.png" width="100%">
          <div class="example">
            <p>{{ this.result.name[1][2] }}</p>
          </div>
        </div>
      </b-col>
    </b-row>
    <b-row>
      <div>
        <img src="@/assets/name_img/cal.jpg" width="100%">
        <div class="cexample f-ujr" style="top: 30%; left: 15%;"> {{ this.result.cal[0][1][0] }}</div>
        <div class="cexample f-ujr" style="top: 30%; left: 33%;"> {{ this.result.cal[0][1][1] }}</div>
        <div class="cexample f-ujr" style="top: 30%; left: 50%;"> {{ this.result.cal[0][1][2] }}</div>
        <div class="cexample f-ujr" style="top: 30%; left: 70%;"> {{ this.result.cal[0][1][3] }}</div>
        <div class="cexample f-ujr" style="top: 30%; left: 90%;"> {{ this.result.cal[0][1][4] }}</div>
      </div>
    </b-row>
    <!-- <div style="width: 90px; float: left"> div tag
      <img src="@/assets/circle6.png" width="100%">
      <div style="text-align: center; position: absolute; top: 10%; left: 13%;  font-size: 2em;">
        <p>{{ this.result.name[0][0] }}</p>
      </div>
    </div> -->
    <div style="width: 500px; margin: auto"></div>
    <NameCompatibilityResultShare style="margin: 50px" />
  </b-container>
</template>

<script>
import NameCompatibilityResultShare from "@/components/NameCompatibilityResultShare.vue";
import axios from "axios";

const URL = "http://127.0.0.1:8000/services/name_compability/"

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
        console.log(res.data)
      })
    }
  }
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
    transform: translate( -50%, -50% );
  }

  @media screen and (min-width: 768px) {
    div.example {
      font-size: 25px;
      text-align: center;
      position: absolute;
      top: 63%;
      left: 50%;
      transform: translate( -50%, -50% );
    }
  }

  @media screen and (max-width: 768px) {
    div.example {
      font-size: 20px;
      text-align: center;
      position: absolute;
      top: 63%;
      left: 50%;
      transform: translate( -50%, -50% );
    }
  }

  @media screen and (min-width: 768px) {
    div.cexample {
      font-size: 25px;
      text-align: center;
      position: absolute;
      transform: translate( -50%, -50% );
    }
  }

  @media screen and (max-width: 768px) {
    div.cexample {
      font-size: 20px;
      text-align: center;
      position: absolute;
      transform: translate( -50%, -50% );
    }
  }
  
</style>
