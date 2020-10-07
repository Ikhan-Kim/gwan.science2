<template>
  <div>
    <img alt="logo" class="logo" src="../assets/main_img/logo.png"/>
    <div class="f-ys h4">관상으로 보는 내 조선시대 신분은?</div>

    <div style="padding-top: 20%">
      <div>
        <router-link to="/FaceReading">
          <button class="main-btn f-ujr" squared variant="outline-secondary">
            제 ＜1＞ 법칙. 관 상 분 석
          </button>
        </router-link>
      </div>
      <div>

      <router-link to="/NameCompatibility">
        <button class="main-btn f-ujr" squared variant="outline-secondary">
          제 ＜2＞ 법칙. 이 름 궁 합
        </button>
      </router-link>
     </div>
    <div>
      <router-link to="/LifeClock">
        <button class="main-btn f-ujr" squared variant="outline-secondary">
          제 ＜3＞ 법칙. 인 생 시 계
        </button>
      </router-link>
    </div>
    <!-- <div style="padding-bottom:100px">
      <router-link to="/Builders">
        <button class="main-btn f-ujr" squared variant="outline-secondary">
          제 ＜4＞ 법칙. 만든사람들
        </button>
      </router-link>
    </div> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
</script>

<style>
.logo {
  padding-top: 20%;
  max-width: 80%;
  max-height: 20%;
}

.main-btn {
  padding-left: 10%;
  padding-right: 10%;
  max-width: 80%;
  max-height: 20%;
  margin-bottom: 5%;
  display: inline-block;
  font-weight: 400;
  color: #212529;
  text-align: center;
  vertical-align: middle;
  user-select: none;
  background-color: white;
  border: 1px dashed transparent;
  border-width: 3px;
  border-color: black;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
