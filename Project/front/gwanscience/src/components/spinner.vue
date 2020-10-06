<template>
  <div v-if="!loading" style="height: 500px">
    <div class="d-flex justify-content-center mb-3" style="margin-top: 200px">
      <b-spinner label="Loading..."></b-spinner>
    </div>
    <strong>{{ loadingMent }}</strong>
    <!-- <div class="d-flex align-items-center">
      <strong>Loading...</strong>
      <b-spinner class="ml-auto"></b-spinner>
    </div> -->
  </div>
</template>

<script>
export default {
  props: {
    loading: {
      type: Boolean,
      required: true,
    },
    loadingMent: {
      type: String,
      required: true,
    }
  }
}
</script>

<style>

</style>