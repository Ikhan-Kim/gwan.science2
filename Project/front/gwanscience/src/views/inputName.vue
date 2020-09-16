<template>
  <div>
    <h1>이름 궁합</h1>
    <div style="margin: 50px"></div>
    <div class="row d-flex justify-content-center m-md-2">
      <b-form-input  class="col-md-6" type="text" placeholder="본인의 이름을 입력해주세요."></b-form-input>
    </div>
    <div class="row d-flex justify-content-center m-md-2">
      <b-form-input  class="col-md-6" type="text" placeholder="상대방의 이름을 입력해주세요."></b-form-input>
    </div>
    <div style="margin: 80px"></div>
    <router-link to="/name-compatibility">
      <b-button style="width: 200px" squared variant="outline-secondary">계산하기</b-button>
    </router-link>



  </div>

</template>

<script>
export default {
  name: "inputName"
}
</script>

<style scoped>

</style>