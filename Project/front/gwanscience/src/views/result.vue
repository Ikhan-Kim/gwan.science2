<template>
  <div>
    <h1>{{ userInfo.nickname }}님의 관상 분석 결과</h1>
    <hr />
    <div style="width: 500px; margin: auto">
      <img :src="userInfo.userPhoto" />
      <h2 style="font-family: 궁서; font-weight: bold; margin-top: 30px">
        왕의 상
      </h2>
      <p>용맹스럽고 위엄이 있으며 먹고 사는데 큰 지장이 없다.</p>
      <h3 style="margin-top: 30px">눈썹</h3>
      <h5>숱이 짙음, 위를 향함</h5>
      <p>
        이성을 놀이상대로 보지 않음, 통솔력이 좋고 믿음직함, 의리가 좋은 편,
        재운과 명예운이 좋음, 너무 두꺼우면 공격적일수 있음. 분명하고 확실한
        성격
      </p>
      <h3 style="margin-top: 30px">미간</h3>
      <h5>미간이 넓음</h5>
      <p>이해심이 넓어 대인관계가 좋음.</p>
      <h3 style="margin-top: 30px">눈</h3>
      <h5>작은 눈, 눈꼬리가 올라감, 눈 사이가 멂</h5>
      <p>
        건실하며 대기만성형 성격이 있으며 주로 자수성가형, 어려움에 당당히 맞설
        수 있는 당찬 기질, 자신에 대한 믿음이 강하고 실행력이 뛰어나 많은
        사람들, 주변인의 지지와 신임을 얻는 편, 적극적이면서 명랑하고 정직,
        용기가 있으며 자수성가, 자존심이 강해 지는 것을 싫어함, 책임감이 강함,
        자신의 영역을 침범받는 것을 싫어하고 자기 방어적인 면을 가지고있음,
        마음이 넓고 정도가 깊음, 가는 사람 붙잡지 않고 멋 곳을 지향
      </p>
      <h3 style="margin-top: 30px">코</h3>
      <h5>긴 코</h5>
      <p>
        사고력과 이해력이 풍부, 도덕성이 뛰어나고 규칙적이나 실천력이 부족하고
        이론에만 치우치는 경우가 있음, 고상한 것을 좋아함
      </p>
      <h3 style="margin-top: 30px">인중</h3>
      <h5>긴 인중</h5>
      <p>
        참을성이 많고 덕이 많음, 감정적인 부분이 많고, 한번 사귄 사람과 관계를
        오래 유지
      </p>
      <h3 style="margin-top: 30px">입</h3>
      <h5>큰 입</h5>
      <p>포용력이 있고 행동력과 리더쉽이 있음, 부귀와 장수를 나타냄</p>
      <h3 style="margin-top: 30px">얼굴형</h3>
      <h5>긴 얼굴형</h5>
      <p>
        이기적이고 독단적인 사람이라고 평가받기 쉬움, 의욕이 강하고 자신감이
        있음, 독립심이 강해 어떤 일도 혼자의 힘으로 밀어 붙이는 경우가 종종
        있음, 인내력이 강하고 지도자가 될 가능성이 있음
      </p>
    </div>
    <ResultShare style="margin: 50px" />
  </div>
</template>

<script>
import ResultShare from "@/components/ResultShare.vue";
export default {
  name: "result",
  metaInfo: {},
  props: {
    userInfo: {
      type: Object,
    },
  },
  components: {
    ResultShare,
  },
  created() {
    // SDK를 초기화 합니다. 사용할 앱의 JavaScript 키를 설정해 주세요.
    window.Kakao.init("461657f0b2d7529bbc498714486b6b12");

    // SDK 초기화 여부를 판단합니다.
    console.log(window.Kakao.isInitialized());
  },
};
</script>

<style scoped></style>
