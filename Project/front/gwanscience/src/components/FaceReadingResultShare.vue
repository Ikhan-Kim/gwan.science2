<template>

  <b-container>
    <h3 class="f-ujr">내 결과 친구에게 공유하기</h3>
    <b-row class="flex-row m-b300">
    <img
      src="@/assets/images/twitter.png"
      class="shareButtons"
      @click="
        ShareTwitter('http://j3c205.p.ssafy.io/', '관싸이언스: 나의 관상은?')
      "
    >

    <img
      src="@/assets/images/facebook.png"
      class="shareButtons"
      @click="ShareFacebook('http://j3c205.p.ssafy.io/')"
    >
    <img
      src="@/assets/images/kakaostory.png"
      class="shareButtons"
      @click="ShareKakaoStory('http://j3c205.p.ssafy.io/')"
    >

    <img
      src="@/assets/images/blog.png"
      class="shareButtons"
      @click="
        ShareNaverBlog('http://j3c205.p.ssafy.io/', '관싸이언스: 나의 관상은?')
      "
    >

    <img
      src="@/assets/images/kakao.png"
      class="shareButtons"
      @click="ShareKakaoTalk('http://j3c205.p.ssafy.io/')"
    >
</b-row>
  </b-container>
</template>

<script>
export default {
  name: "FaceReadingResultShare",
  metaInfo() {
    return {
      meta: [
        { property: "og:title", content: "관싸이언스: 나의 관상은?" },
        { property: "og:url", content: "http://j3c205.p.ssafy.io/" },
        {
          property: "og:description",
          content:
            "왕의 상: 용맹스럽고 위엄이 있으며 먹고 사는데 큰 지장이 없다.",
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
.shareButtons {
  max-width: 52px;
  max-height: 52px;
  margin-left: 10px;
  margin-right: 10px;
}

.flex-row {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
