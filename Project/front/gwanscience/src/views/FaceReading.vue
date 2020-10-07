<template>
  <div>
    <div v-if="!this.timedelay">
    <div class="f-ujr duru"><h3 class="pt-20">제 ＜1＞ 법칙. 관상분석</h3></div>
    <div class="f-ys" v-if="!isCameraOpen">
      <h5>기본정보를 입력해주세요.</h5>
      <br />
    </div>
    <div class="f-ys" v-else>
      <h5>정확한 관상 분석을 위해 <br />중앙에 얼굴이 오도록 촬영해주세요.</h5>
    </div>

    <br />
    <br />

    <b-container class="bv-example-row f-ujr mb-4" v-if="!isCameraOpen">
      <b-row>
        <b-col cols="4" class="pb-3"><h4>닉네임</h4></b-col>
        <b-col cols="6">
          <b-form-input
            type="text"
            v-model="userInfo.nickname"
            placeholder="닉네임 입력"
          ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="4" class="pb-3"> <h4>나이</h4></b-col>
        <b-col cols="6">
          <b-form-input
            type="number"
            v-model="userInfo.age"
            placeholder="나이 입력"
          ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="4" class="pb-3"> <h4>성별</h4></b-col>
        <b-col cols="6">
          <b-form-radio-group
            v-model="userInfo.gender"
            :options="options"
          ></b-form-radio-group>
        </b-col>
      </b-row>
    </b-container>

    <!-- 📌📌📌 작동 이상 없으면 삭제하기 !! -->
    <!-- <div class="container" v-if="!isCameraOpen">
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-input
          style="width: 300px"
          type="text"
          v-model="userInfo.nickname"
          placeholder="닉네임을 입력해주세요."
        ></b-form-input>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-input
          style="width: 300px"
          type="number"
          v-model="userInfo.age"
          placeholder="나이를 입력해주세요."
        ></b-form-input>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-select
          style="width: 300px"
          v-model="userInfo.gender"
          :options="options"
        ></b-form-select>
      </div>
    </div> -->

    <!-- 사진촬영 버튼 -->

    <div class="container">
      <div class="row d-flex justify-content-center">
        <button
          v-if="!isCameraOpen"
          class="btn-customm bg-red f-ujr mb-3"
          style="width: 60%"
          :class="{
            'bg-red': !isCameraOpen,
            'bg-green': isCameraOpen,
          }"
          @click="checkInfo"
        >
          <span class="bg-red h4 mt-3">사진 촬영</span>
        </button>

        <!-- <input type="file" accept="image/*" capture="camera" /> -->

        <!-- <button @click="splitFace">얼굴쪼개기</button> -->
        <!-- <div class="camera-button"></div> -->
      </div>
      <!-- <div class="row d-flex justify-content-center m-md-2"> -->
      <div class="camera-box" v-if="isCameraOpen">
        <video
          v-show="!isPhotoTaken"
          ref="camera"
          id="Taken"
          :width="300"
          :height="225"
          autoplay
        ></video>
        <div class="example" style="width: 250px" v-if="!isPhotoTaken">
          <img src="@/assets/main_img/face_outline.png" width="58%" />
        </div>
        <canvas
          v-show="isPhotoTaken"
          ref="canvas"
          id="photoTaken"
          :width="300"
          :height="225"
        ></canvas>
      </div>
      <!-- </div> -->

      <div class="camera-shoot mt-4 mb-5" v-if="isCameraOpen">
        <button
          v-if="isPhotoTaken == false"
          class="btn-customm bg-red f-ujr h4"
          style="width: 60%"
          @click="takePhoto"
        >
          사진촬영
        </button>

        <button
          v-if="isPhotoTaken == true"
          class="btn-customm bg-green f-ujr mr-4 h5"
          style="width: 30%"
          @click="takePhoto"
        >
          다시찍기
        </button>
        <button
          v-if="isPhotoTaken == true"
          class="btn-customm f-ujr bg-red h5"
          style="width: 30%"
          @click="sendImage()"
        >
          관상보기
        </button>
      </div>

      <!-- <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot"  v-if="isPhotoTaken">
          <canvas id="userPhoto" :width="300" :height="300"></canvas>
        </div>
      </div> -->
    </div>
    </div>
    <spinner :loading="this.timedelay" :loadingMent="this.loadMent"></spinner>
  </div>
</template>

<script>
import axios from "axios";
import spinner from "@/components/spinner.vue";

export default {
  name: "FaceReading",
  data() {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      timedelay: false,
      loadMent: "관상을 분석중입니다...",
      userInfo: {
        nickname: "",
        age: null,
        gender: null,
        userPhoto: null,
      },
      options: [
        // { value: null, text: "성별을 선택해주세요.", disabled: true },
        { value: 1, text: "남자" },
        { value: 2, text: "여자" },
      ],
      result: {
        username: null,
        eyebrowShape: null,
        eyebrowInterval: null,
        eyeSize: null,
        eyeInterval: null,
        eyeTail: null,
        noseLength: null,
        noseWidth: null,
        mouthLength: null,
        mouthThickness: null,
        mouthTail: null,
        eyebrowResult: null,
        eyeResult: null,
        noseResult: null,
        mouthResult: null,
        totalResult: null,
      },
      // tmpphoto: null,
    };
  },

  components: {
    spinner,
  },

  methods: {
    checkInfo() {
      if (this.userInfo.nickname == "") {
        alert("닉네임을 입력해 주세요.");
      } else if (this.userInfo.age == null) {
        alert("나이를 입력해 주세요.");
      } else if (this.userInfo.gender == null) {
        alert("성별을 선택해 주세요.");
      } else {
        alert(
          "아이폰은 일시정지 버튼 클릭 후, 왼쪽 상단의 ❌ 버튼을 클릭하면 사진이 촬영 됩니다."
        );
        this.toggleCamera();
      }
    },
    checkAge() {
      if (this.userInfo.age < 1) {
        alert("1 이상의 정수를 입력 해주세요");
      }
    },
    toggleCamera() {
      if (this.isCameraOpen) {
        this.isCameraOpen = false;
        this.isPhotoTaken = false;
        this.stopCameraStream();
      } else {
        this.isCameraOpen = true;
        this.createCameraElement();
      }
    },
    createCameraElement() {
      const constraints = (window.constraints = {
        audio: false,
        video: true,
      });

      navigator.mediaDevices
        .getUserMedia(constraints)
        .then((stream) => {
          this.$refs.camera.srcObject = stream;
        })
        .catch((err) => {
          console.log(err);
          alert("설정을 확인해주세요.");
        });
    },
    stopCameraStream() {
      let tracks = this.$refs.camera.srcObject.getTracks();

      tracks.forEach((track) => {
        track.stop();
      });
    },
    takePhoto() {
      this.isPhotoTaken = !this.isPhotoTaken;

      const context = this.$refs.canvas.getContext("2d");
      context.drawImage(this.$refs.camera, 0, 0, 300, 225);

      // console.log(context.canvas.toDataURL());
      // this.userInfo.userPhoto = context.canvas.toDataURL();
      this.userInfo.userPhoto = document
        .getElementById("photoTaken")
        .toDataURL("image/jpeg");
      // console.log(this.tmpphoto);
    },

    sendImage() {
      this.timedelay = true
      axios
        .post(
          `https://j3c205.p.ssafy.io/api/services/face_reading/`,
          // `http://127.0.0.1:8000/api/services/face_reading/`,
          this.userInfo
        )
        .then((res) => {
          console.log("보내짐");
          this.result = res.data;
          console.log("test", this.result);
          this.$router.push({
            name: "FaceReadingResult",
            params: {
              username: this.userInfo.nickname,
              eyebrowShape: this.result.eyebrowShape,
              eyebrowInterval: this.result.eyebrowInterval,
              eyeSize: this.result.eyeSize,
              eyeInterval: this.result.eyeInterval,
              eyeTail: this.result.eyeTail,
              noseLength: this.result.noseLength,
              noseWidth: this.result.noseWidth,
              mouthLength: this.result.mouthLength,
              mouthThickness: this.result.mouthThickness,
              mouthTail: this.result.mouthTail,
              eyebrowResult: this.result.eyebrowResult,
              eyeResult: this.result.eyeResult,
              mouthResult: this.result.mouthResult,
              noseResult: this.result.noseResult,
              job: this.result.job,
            },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // splitFace() {
    //   axios.get(`http://127.0.0.1:8000/services/split`)
    //   .then(res => {
    //     console.log(res)
    //     console.log('얼굴을 쪼갬')
    //   })
    // }
  },
};
</script>

<style>
.duru {
  background-image: url(../assets/main_img/duru.png);
  background-size: cover;
  background-repeat: no-repeat;
  width: 360px;
  height: 80px;
  margin: 0 auto;
}

.pt-20 {
  padding-top: 20px;
}

.btn-customm {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  vertical-align: middle;
  background-color: (192, 0, 0);
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
/* :width="300" */
/* :height="300" */
.img-size {
  width: 300px;
  height: 300px;
}
.example {
  text-align: center;
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
