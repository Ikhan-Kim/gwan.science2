<template>
  <div>
    <LifeClockResultComponent :result="result" />
  </div>
</template>

<script>
import axios from "axios";
import LifeClockResultComponent from "@/components/LifeClockResultComponent";

const URL = "http://127.0.0.1:8000/services/life_clock/";

export default {
  name: "LifeClockResult",
  components: {
    LifeClockResultComponent,
  },
  data() {
    return {
      result: {
        time: null,
        ment: null,
        img_url: null,
      },
    };
  },
  created() {
    this.loadResult();
  },
  methods: {
    loadResult() {
      axios.get(URL + this.$route.params.age).then((res) => {
        this.result = res.data;
        console.log(this.result.img_url);
      });
    },
  },
};
</script>

<style>
</style>