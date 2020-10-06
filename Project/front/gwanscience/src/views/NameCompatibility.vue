<template>
  <div>
    <img src="../assets/name_img/head.png" width="400px">
    <div style="margin: 50px"></div>
    <div style="padding-bottom: 200px">
      <div class="left">
        <p class="name" style="margin-top: 7px">내 이름</p>
        <p class="name">상대방 이름</p>
      </div>
      <div class="right">
        <input
            v-model="name1"
            type="text"
            style="margin: 0px 20px 5px 0px"
        />
        <br>
        <input
            v-model="name2"
            style="margin: 0px 20px 5px 0px"
            type="text"
        />
      </div>
    </div>
    <router-link to="/name-compatibility">
      <img src="../assets/name_img/ok.png" style="width: 300px">
    </router-link>
    <div style="padding-bottom: 300px"></div>
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