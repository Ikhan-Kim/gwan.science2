<template>
  <div>
    <h1>{{userInfo.nickname}}님의 관상 분석 결과</h1>
    <div>
      <b-tabs content-class="mt-3">
        <b-tab title="눈">
          <p></p>
        </b-tab>
        <b-tab title="눈썹">
          <p></p>
        </b-tab>
        <b-tab title="코">
          <p></p>
        </b-tab>
        <b-tab title="입">
          <p></p>
        </b-tab>
        <b-tab title="종합 평가" active>
          <p></p>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
export default {
  name: "result",
  props: {
    userInfo: {
      type: Object,
    },
  },
};
</script>

<style scoped>
</style>