<template>
  <div>
    <p>
      {{ this.result.name[0] }}님이 {{ this.result.name[1] }}님을 {{ this.result.score[0] }} 정도 좋아합니다.
    </p>
    <p>
      {{ this.result.name[1] }}님이 {{ this.result.name[0] }}님을 {{ this.result.score[1] }} 정도 좋아합니다.
    </p>
  </div>
</template>

<script>
import axios from "axios"

const URL = "http://127.0.0.1:8000/services/test/"

export default {
  name: "resultName",

  data () {
    return {
      result: {
        name: [null, null],
        score: [null, null],
      }
    }
  },

  created() {
    this.loadresult();
  },

  methods: {
    loadresult() {
      axios.get(URL + this.$route.params.name1 + '/' + this.$route.params.name2)
      .then(res => {
        this.result = res.data
      })
    }
  }
}
</script>
