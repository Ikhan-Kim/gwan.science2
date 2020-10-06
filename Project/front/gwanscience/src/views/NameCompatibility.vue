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
    <button @click="inputName" class="bg-red btn-customm f-ujr m-b300"
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
      this.$router.push({
        name: "NameCompatibilityResult",
        params: {
          name1: this.name1,
          name2: this.name2,
        },
      });
    },
  },
};
</script>

<style scoped>
</style>