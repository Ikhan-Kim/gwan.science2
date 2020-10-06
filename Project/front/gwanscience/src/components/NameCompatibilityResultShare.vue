<template>
  <b-container>
    <h3 class="f-ujr">내 결과 친구에게 공유하기</h3>
    <b-row>
      <img
        src="@/assets/main_img/twitter.png"
        class="shareButtons"
        @click="
          ShareTwitter(
            `https://j3c205.p.ssafy.io/${name1}/${name2}`,
            '관싸이언스: 우리의 궁합은?')
        "
      >
      <img
        src="@/assets/main_img/facebook.png"
        class="shareButtons"
        @click="ShareFacebook(`https://j3c205.p.ssafy.io/${name1}/${name2}`)"
      >
      <img
        src="@/assets/main_img/kakaostory.png"
        class="shareButtons"
        @click="ShareKakaoStory(`https://j3c205.p.ssafy.io/${name1}/${name2}`)"
      >
      <img
        src="@/assets/main_img/blog.png"
        class="shareButtons"
        @click="
          ShareNaverBlog(
            `https://j3c205.p.ssafy.io/${name1}/${name2}`,
            '관싸이언스: 우리의 궁합은?')"
      >
      <img
        src="@/assets/main_img/kakao.png"
        class="shareButtons"
        @click="ShareKakaoTalk(`https://j3c205.p.ssafy.io/${name1}/${name2}`)"
      >
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "FaceReadingResultShare",
  data() {
    return {
      name1: this.$parent.name1,
      name2: this.$parent.name2,
    };
  },
  metaInfo() {
    return {
      meta: [
        {
          property: "og:description",
          content: "내가 생각하는 너의 마음, 네가 생각 하는 나의 마음.",
        },
        { property: "og:image", content: "../assets/img.jpg" },
      ],
    };
  },
  methods: {
    ShareTwitter(url, text) {
      window.open(
        "http://twitter.com/intent/tweet?url=" + url + "&text=" + text
      );
    },
    ShareFacebook(url) {
      window.open("http://www.facebook.com/sharer/sharer.php?u=" + url);
    },
    ShareKakaoStory(url) {
      window.open("http://story.kakao.com/share?url=" + url);
    },
    ShareNaverBlog(url, title) {
      window.open(
        "http://blog.naver.com/openapi/share?url=" + url + "&title=" + title
      );
    },
    ShareKakaoTalk(url) {
      window.Kakao.Link.sendScrap({
        requestUrl: url,
      });
    },
  },
};
</script>

<style>
/* .shareButtons {
  display: block;
  margin: 25px auto 25px auto;
} */
</style>
