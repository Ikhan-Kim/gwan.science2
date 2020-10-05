<template>
  <div>
    <h2>결과 공유하기</h2>
    <button
      class="shareButtons"
      @click="
        ShareTwitter(
          `http://j3c205.p.ssafy.io/${name1}/${name2}`,
          '관싸이언스: 우리의 궁합은?'
        )
      "
    >
      트위터 공유하기
    </button>
    <button
      class="shareButtons"
      @click="ShareFacebook(`http://j3c205.p.ssafy.io/${name1}/${name2}`)"
    >
      페이스북 공유하기
    </button>
    <button
      class="shareButtons"
      @click="ShareKakaoStory(`http://j3c205.p.ssafy.io/${name1}/${name2}`)"
    >
      카카오스토리 공유하기
    </button>
    <button
      class="shareButtons"
      @click="
        ShareNaverBlog(
          `http://j3c205.p.ssafy.io/${name1}/${name2}`,
          '관싸이언스: 우리의 궁합은?'
        )
      "
    >
      네이버 블로그 공유하기
    </button>
    <button
      class="shareButtons"
      @click="ShareKakaoTalk(`http://j3c205.p.ssafy.io/${name1}/${name2}`)"
    >
      카카오톡 공유하기
    </button>
  </div>
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
