<template>
  <div>
    <div class="f-ujr duru"><h3 class="pt-20"> 제 ＜3＞ 법칙. 인생시계</h3></div>
    <div class="f-ys"><h5>당신의 인생은 지금 몇 시 일까요?</h5><br></div>

    <b-container class="bv-example-row f-ujr" v-if="!isCameraOpen">
      <b-row>
        <b-col cols="4" class="pb-3"><h4>나이</h4></b-col>
        <b-col cols="8">
          <b-form-input
          type="number"
        v-model="userInfo.age"
        placeholder="나이를 입력해주세요."
        ></b-form-input>
        </b-col>
     </b-row>
    </b-container>

    <br>
    <br>
    <br>

      <!-- <router-link
        :to="{ name: 'LifeClockResult', params: { age: userInfo.age } }"
      > -->
      <button @click="goResult" class="bg-red btn-customm f-ujr m-b300"
        >나의 인생 시간 확인하기 ➡</button
      >
      <!-- </router-link> -->
    </div>

</template>

<script>
export default {
  name: "LifeClock",
  data() {
    return {
      userInfo: {
        age: null,
      },
    };
  },
  methods: {
    goResult() {
      if (this.userInfo.age < 1) {
        alert("1 이상의 정수를 입력 해주세요");
      } else if (this.userInfo.age > 80) {
        alert("80 이하의 정수를 입력 해주세요");
      } else {
        this.$router.push({
          name: "LifeClockResult",
          params: {
            age: this.userInfo.age,
          },
        });
      }
    },
  },
};
</script>

<style>
</style>