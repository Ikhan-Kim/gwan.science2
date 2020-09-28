<template>
  <div>
    <h2>결과 공유하기</h2>
    <button
      class="shareButtons"
      @click="
        ShareTwitter('http://j3c205.p.ssafy.io/', '관싸이언스: 나의 관상은?')
      "
    >
      트위터 공유하기
    </button>
    <button
      class="shareButtons"
      @click="ShareFacebook('http://j3c205.p.ssafy.io/')"
    >
      페이스북 공유하기
    </button>
    <button class="shareButtons">카카오톡 공유하기</button>
  </div>
</template>

<script>
export default {
  name: "ResultShare",
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
  },
};
</script>

<style>
.shareButtons {
  display: block;
  margin: 25px auto 25px auto;
}
</style>
