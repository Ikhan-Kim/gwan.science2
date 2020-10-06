<template>
  <div>
    <div class="f-ujr duru"><h3 class="pt-20"> 제 ＜2＞ 법칙. 이름궁합</h3></div>
    <div class="f-ys"><h5>상대방과 이름궁합을 확인하세요.</h5><br></div>
    <div style="margin: 50px"></div>
    <b-container class="bv-example-row f-ujr">
      <b-row>
        <b-col cols="4" class="pb-3"><h4>내 이름</h4></b-col>
        <b-col cols="8">
          <b-form-input
              v-model="name1"
              style="width: 300px"
              type="text"
              placeholder="본인의 이름을 입력해주세요."
          ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="4" class="pb-3"><h4> 상대방 이름</h4></b-col>
        <b-col cols="8">
          <b-form-input
              v-model="name2"
              style="width: 300px"
              type="text"
              placeholder="본인의 이름을 입력해주세요."
          ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="8">
        </b-col>
      </b-row>
    </b-container>

    <div style="margin: 80px"></div>
    <!--    <router-link to="/NameCompatibilityResult">-->
    <button @click="inputName" class="bg-red btn-customm f-ujr"
    >궁합 확인하기
    </button
    >
    <!--    </router-link>-->
  </div>
</template>

<script>
export default {
  name: "NameCompatibility",

  data() {
    return {
      name1: null,
      name2: null,
    };
  },

  methods: {

    inputName() {
      var pattern = /([^가-힣\x20])/i;
      if (pattern.test(this.name1)||pattern.test(this.name2)) {
        alert("한글이 아닙니다. (자음, 모음만 있는 한글은 처리하지 않습니다.)");
      } else if (this.name1.length != 3 || this.name2.length != 3)
        alert("세 글자 이름만 입력 해주세요.")
      else {
        this.$router.push({
          name: "NameCompatibilityResult",
          params: {
            name1: this.name1,
            name2: this.name2,
          },
        });
      }
    },
  },
};
</script>

<style>
div.left {
  width: 40%;
  float: left;
  box-sizing: border-box;
}

div.right {
  width: 60%;
  float: right;
  box-sizing: border-box;
}

input {
  width: 200px;
  height: 40px;
  border-radius: 5px;
  border-width: 1px;
}

p.name {
  text-align: center;
  margin-bottom: 20px;
  font-family: BMEULJIRO;
  font-size: 20px;
}
</style>