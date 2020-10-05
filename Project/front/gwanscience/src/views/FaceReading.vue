<template>
  <div style="margin-top: 150px">
    <h1>Face Reading</h1>
    <div class="container" v-if="!isCameraOpen">
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
    </div>
    <div class="container">
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-button">
          <b-button
            class="btn-success"
            :class="{
              'btn-success': !isCameraOpen,
              'btn-danger': isCameraOpen,
            }"
            @click="toggleCamera"
          >
            <span v-if="!isCameraOpen">사진 촬영</span>
            <span v-else>취소</span>
          </b-button>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-box" v-if="isCameraOpen">
          <video
            v-show="!isPhotoTaken"
            ref="camera"
            id="Taken"
            :width="450"
            :height="300"
            autoplay
          ></video>
          <canvas
            v-show="isPhotoTaken"
            ref="canvas"
            id="photoTaken"
            :width="450"
            :height="300"
          ></canvas>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot" v-if="isCameraOpen">
          <b-button class="btn-success" @click="takePhoto">사진촬영</b-button>
          <b-button
            v-if="isPhotoTaken == true"
            style="margin-left: 20px"
            @click="imgToBack()"
            >관상보기</b-button
          >
        </div>
      </div>
      <div>
        <button v-if="isPhotoTaken" @click="sendImage">사진보내기 test</button>
      </div>
      <!-- <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot"  v-if="isPhotoTaken">
          <canvas id="userPhoto" :width="450" :height="300"></canvas>
        </div>
      </div>-->
    </div>
  </div>
</template>

<script>
import axios from "axios";
const URL = "http://127.0.0.1:8000/services/face_reading/";
export default {
  name: "FaceReading",
  data() {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      userInfo: {
        nickname: "",
        age: null,
        gender: null,
        userPhoto: null,
      },
      options: [
        { value: null, text: "성별을 선택해주세요.", disabled: true },
        { value: 1, text: "남자" },
        { value: 2, text: "여자" },
      ],
      result: {
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
      tmpphoto: null,
    };
  },

  methods: {
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
      context.drawImage(this.$refs.camera, 0, 0, 450, 300);

      // console.log(context.canvas.toDataURL());
      this.userInfo.userPhoto = context.canvas.toDataURL();
      this.tmpphoto = document.getElementById("photoTaken").toDataURL("image/jpeg");

      // 아래 코드 수정 예정

      // const context = this.$refs.canvas.getContext('2d')

      // const photo = document.getElementById("photoTaken").toDataURL("image/jpeg")
      // .replace("image/jpeg", "image/octet-stream")

      // this.photo = canvas.drawImage(photo)
      // this.photo = this.$refs.canvas.getContext('2d')
      // this.photo = context.drawImage(this.$refs.camera, 0,0,450,300)
      //  = context.getImageData( 0,0,450,300)

      // const photo = document.getContext("2d").toDataURL("image/jpeg")
      // const userPhoto = document.getElementById("userPhoto").getContext("2d")
      // userPhoto.drawImage(photo, 0,0,450,300)

      // const canvas = document.getElementById("photoTaken").toDataURL("image/jpeg")
      // .replace("image/jpeg", "image/octet-stream");
      // const userPhoto = document.getElementById("userPhoto").getContext("2d")
      // userPhoto.drawImage(canvas, 0, 0, 450, 300);
    },

    // downloadImage() {
    // const download = document.getElementById("downloadPhoto");
    // const canvas = document.getElementById("photoTaken").toDataURL("image/jpeg")
    //   .replace("image/jpeg", "image/octet-stream");

    // download.setAttribute("href", canvas);
    // }
    imgToBack() {
      axios.get(URL + this.userInfo.nickname).then((res) => {
        this.result = res.data;
        console.log(this.result);
        this.$router.push({
          name: "FaceReadingResult",
          params: {
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
          },
        });
      });
    },
    sendImage() {
      axios.post(`http://127.0.0.1:8000/services/test`, this.tmpphoto)
      .then(res=> {
        console.log(res)
        console.log('보내짐')
      })
      .catch(err=> {
        console.log(err)
      })
    },
  },
};
</script>

<style>
</style>
