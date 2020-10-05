<template>
  <div>
    <div class="f-ujr duru"><h3 class="pt-20"> 제 ＜1＞ 법칙. 관상분석</h3></div>
    <div class="f-ys" v-if="!isCameraOpen"><h5>기본정보를 입력해주세요.</h5><br></div>
    <div class="f-ys" v-else><h5>정확한 관상 분석을 위해 <br>중앙에 얼굴이 오도록 촬영해주세요.
</h5></div>
    
    <br>
    <br>

    <b-container class="bv-example-row f-ujr" v-if="!isCameraOpen">
      <b-row >
        <b-col cols="4" class="pb-3"><h4> 닉네임</h4></b-col>
        <b-col cols="8">
          <b-form-input
          type="text"
          v-model="userInfo.nickname"
          placeholder="닉네임을 입력해주세요."
        ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="4" class="pb-3"> <h4> 나이</h4></b-col>
        <b-col cols="8">
          <b-form-input
          type="number"
          v-model="userInfo.age"
          placeholder="나이를 입력해주세요."
        ></b-form-input>
        </b-col>
        <div class="w-100"></div>
        <b-col cols="4" class="pb-3"> <h4> 성별</h4></b-col>
        <b-col cols="8">
          <b-form-radio-group
          v-model="userInfo.gender"
          :options="options"
        ></b-form-radio-group>
        </b-col>
     </b-row>
    </b-container>

    <!-- 사진 촬영 버튼 -->
    
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
      <div class="row d-flex justify-content-center m-md-2">
        
          <b-button v-if="!isCameraOpen" 
            class=" btn-danger f-ujr"
            :class="{
              'btn-danger': !isCameraOpen,
              'btn-success': isCameraOpen,
            }"
            @click="toggleCamera"
          >
            <span class="btn-danger">사진 촬영</span>
          </b-button>
        <div class="camera-button"></div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-box" v-if="isCameraOpen">
          <video
            v-show="!isPhotoTaken"
            ref="camera"
            id="Taken"
            :width="300"
            :height="300"
            autoplay
          ></video>
          <canvas
            v-show="isPhotoTaken"
            ref="canvas"
            id="photoTaken"
            :width="300"
            :height="300"
          ></canvas>
        </div>
      </div>
      <div class="row d-flex justify-content-center">
        <div class="camera-shoot" v-if="isCameraOpen">
          <b-button class="btn-success f-ujr" @click="takePhoto">사진촬영</b-button>
          <router-link
            :to="{ name: 'FaceReadingResult', params: { userInfo: userInfo } }"
          >
            <button v-if="isPhotoTaken == true" class="btn-customm f-ujr"
              >관상보기</button
            >
          </router-link>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot"  v-if="isPhotoTaken">
          <canvas id="userPhoto" :width="300" :height="300"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
        // { value: null, text: "성별을 선택해주세요.", disabled: true },
        { value: 1, text: "남자" },
        { value: 2, text: "여자" },
      ],
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
      context.drawImage(this.$refs.camera, 0, 0, 300, 300);

      // console.log(context.canvas.toDataURL());
      this.userInfo.userPhoto = context.canvas.toDataURL();

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
  },
};
</script>

<style>
.duru {
  background-image: url(../assets/images/duru.png);
  background-size: cover;
  background-repeat: no-repeat;
  width: 360px;
  height: 80px;
  margin: 0 auto;
}

.pt-20 {
  padding-top:  20px;
}

.btn-customm {
    display: inline-block;
    font-weight: 400;
    text-align: center;
    vertical-align: middle;
    user-select: none;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.25rem;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
