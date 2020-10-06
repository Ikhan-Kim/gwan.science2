<template>
  <div>
    <div class="f-ujr duru"><h3 class="pt-20"> 제 ＜3＞ 법칙. 인생시계</h3></div>
    <div class="f-ys">
      <div style="margin-bottom: 50px"></div>
      <h6 style="width: 80%; margin-left: 10%" >사람의 평균 수명을 80세로 잡고 하루 24시간을 환산한다면 하루가 1440분,
        이것을 다시 80으로 나누면 18분이라는 시간이 나옵니다.
        즉, 1년의 시간은 하루의 18분이라는 셈이죠.
        당신의 인생시계는 지금 몇시인가요?</h6><br></div>

    <br>
    <br>
    <br>
    <b-container class="bv-example-row f-ujr" v-if="!isCameraOpen">
      <b-row>
        <b-col cols="4" class="pb-3"><h4>나이</h4></b-col>
        <b-col cols="6">
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
    <button @click="goResult" class="bg-red btn-customm f-ujr"
    >나의 인생 시간 확인하기 ➡
    </button
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