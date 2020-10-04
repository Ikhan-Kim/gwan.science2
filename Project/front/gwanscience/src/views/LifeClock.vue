<template>
  <div>
    <h1>Life Clock</h1>
    <div class="row d-flex justify-content-center m-md-2">
      <b-form-input
        style="width: 300px"
        type="number"
        v-model="userInfo.age"
        placeholder="나이를 입력해주세요."
      ></b-form-input>
      <router-link
        :to="{ name: 'LifeClockResult', params: { age: userInfo.age } }"
      >
        <b-button style="margin-left: 20px">나의 인생 시간은? →</b-button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "LifeClock",
  data() {
    return {
      userInfo: {
        age: 0,
      },
    };
  },
};
</script>

<style>
</style>