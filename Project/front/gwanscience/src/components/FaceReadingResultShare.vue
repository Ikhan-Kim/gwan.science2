<template>
  <b-container>
    <h3 class="f-ujr">내 결과 친구에게 공유하기</h3>
    <b-row class="flex-row">
      <img
        src="@/assets/main_img/twitter.png"
        class="shareButtons"
        @click="
          ShareTwitter(
            `https://j3c205.p.ssafy.io/FaceReading/${result.username}/${result.eyebrowShape}/${result.eyebrowInterval}/${result.eyeSize}/${result.eyeInterval}/${result.eyeTail}/${result.noseLength}/${result.noseWidth}/${result.mouthLength}/${result.mouthThickness}/${result.mouthTail}`,
            '관싸이언스: 나의 관상은?'
          )
        "
      />

      <img
        src="@/assets/main_img/facebook.png"
        class="shareButtons"
        @click="
          ShareFacebook(
            `https://j3c205.p.ssafy.io/FaceReading/${result.username}/${result.eyebrowInterval}/${result.eyeSize}/${result.eyeInterval}/${result.eyeTail}/${result.noseLength}/${result.noseWidth}/${result.mouthLength}/${result.mouthThickness}/${result.mouthTail}`
          )
        "
      />
      <img
        src="@/assets/main_img/kakaostory.png"
        class="shareButtons"
        @click="
          ShareKakaoStory(
            `https://j3c205.p.ssafy.io/FaceReading/${result.username}/${result.eyebrowInterval}/${result.eyeSize}/${result.eyeInterval}/${result.eyeTail}/${result.noseLength}/${result.noseWidth}/${result.mouthLength}/${result.mouthThickness}/${result.mouthTail}`
          )
        "
      />

      <img
        src="@/assets/main_img/blog.png"
        class="shareButtons"
        @click="
          ShareNaverBlog(
            `https://j3c205.p.ssafy.io/FaceReading/${result.username}/${result.eyebrowInterval}/${result.eyeSize}/${result.eyeInterval}/${result.eyeTail}/${result.noseLength}/${result.noseWidth}/${result.mouthLength}/${result.mouthThickness}/${result.mouthTail}`,
            '관싸이언스: 나의 관상은?'
          )
        "
      />

      <img
        src="@/assets/main_img/kakao.png"
        class="shareButtons"
        @click="
          ShareKakaoTalk(
            `https://j3c205.p.ssafy.io/FaceReading/${result.username}/${result.eyebrowInterval}/${result.eyeSize}/${result.eyeInterval}/${result.eyeTail}/${result.noseLength}/${result.noseWidth}/${result.mouthLength}/${result.mouthThickness}/${result.mouthTail}`
          )
        "
      />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "FaceReadingResultShare",
  data() {
    return {
      result: {
        username: this.$parent.result.username,
        eyebrowShape: this.$parent.result.eyebrowShape,
        eyebrowInterval: this.$parent.result.eyebrowInterval,
        eyeSize: this.$parent.result.eyeSize,
        eyeInterval: this.$parent.result.eyeInterval,
        eyeTail: this.$parent.result.eyeTail,
        noseLength: this.$parent.result.noseLength,
        noseWidth: this.$parent.result.noseWidth,
        mouthLength: this.$parent.result.mouthLength,
        mouthThickness: this.$parent.result.mouthThickness,
        mouthTail: this.$parent.result.mouthTail,
      },
    };
  },
  metaInfo() {
    return {
      meta: [
        { property: "og:title", content: "관싸이언스: 나의 관상은?" },
        {
          property: "og:url",
          content: `https://j3c205.p.ssafy.io/FaceReading/${this.result.username}/${this.result.eyebrowShape}/${this.result.eyebrowInterval}/${this.result.eyeSize}/${this.result.eyeInterval}/${this.result.eyeTail}/${this.result.noseLength}/${this.result.noseWidth}/${this.result.mouthLength}/${this.result.mouthThickness}/${this.result.mouthTail}`,
        },
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
  max-width: 40px;
  max-height: 40px;
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
