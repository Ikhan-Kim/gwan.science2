<template>
  <div>
    <h1>Face Reading</h1>
    <div class="container" v-if="!isCameraOpen">
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-input  class="col-md-6" type="text" v-model="userInfo.nickname" placeholder="닉네임을 입력해주세요."></b-form-input>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-input class="col-md-6" type="number" v-model="userInfo.age" placeholder="나이를 입력해주세요."></b-form-input>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <b-form-select class="col-md-6" v-model="userInfo.gender" :options="options"></b-form-select>
      </div>
    </div>
    <div class="container">
      <div class="row  d-flex justify-content-center m-md-2">
        <div class="camera-button">
          <b-button class="btn-success" :class="{ 'btn-success': !isCameraOpen, 'btn-danger': isCameraOpen }" @click="toggleCamera">
            <span v-if="!isCameraOpen">사진 촬영</span>
            <span v-else>촬영 중단</span>
          </b-button>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-box" v-if="isCameraOpen">
          <video v-show="!isPhotoTaken" ref="camera" :width="450" :height="300" autoplay></video>
          <canvas v-show="isPhotoTaken" ref="canvas" id="photoTaken" :width="450" :height="300"></canvas>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot" v-if="isCameraOpen">
          <b-button class="btn-success" @click="takePhoto">사진촬영</b-button>
        </div>
      </div>
      <div class="row d-flex justify-content-center m-md-2">
        <div class="camera-shoot" v-if="isPhotoTaken">
          <b-img :src="photo" :width="450" :height="300"></b-img>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FaceReading',
  data() {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      userInfo: {
        nickname: '',
        age: null,
        gender: null,
      },
      photo: null,
      options: [
        { value: null, text: '성별을 선택해주세요.', disabled: true},
        { value: 1, text: '남자'},
        { value: 2, text: '여자'},
      ]
    }
  },

  methods: {
    toggleCamera() {
      if(this.isCameraOpen) {
        this.isCameraOpen = false
        this.isPhotoTaken = false
        this.stopCameraStream()
      } else {
        this.isCameraOpen = true
        this.createCameraElement()
      }
    },

    createCameraElement() {
      const constraints = (window.constraints = {
        audio: false,
        video: true,
      })

      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
          this.$refs.camera.srcObject = stream
        })
        .catch(err => {
          console.log(err)
          alert("설정을 확인해주세요.")
        })
    },
    stopCameraStream() {
      let tracks = this.$refs.camera.srcObject.getTracks()

      tracks.forEach(track => {
        track.stop()
      })
    },

    takePhoto() {
      this.isPhotoTaken = !this.isPhotoTaken

      const context = this.$resf.canvas.getContext('2d')
      context.drawImage(this.$refs.camera, 0,0,450,300)
      this.photo = context.getImageData( 0,0,450,300)
    }

  }
}
</script>

<style>

</style>
