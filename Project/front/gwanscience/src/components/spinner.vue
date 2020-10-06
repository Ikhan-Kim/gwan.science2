<template>
  <div v-if="!loading" style="height: 500px">
    <div class="d-flex justify-content-center mb-3">
      <b-spinner label="Loading..."></b-spinner>
    </div>
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
    }
  }
}
</script>

<style>

</style>