<template>
  <div>
    <!-- 탭 방식 -->
    <b-tabs content-class="mt-2" class="m-3">
    <b-tab title="눈썹" active><p>I'm the first tab</p></b-tab>
    <b-tab title="눈"><p>I'm the second tab</p></b-tab>
    <b-tab title="코"><p>I'm a disabled tab!</p></b-tab>
    <b-tab title="입"><p>I'm a disabled tab!</p></b-tab>
    <b-tab title="얼굴형"><p>I'm a disabled tab!</p></b-tab>
  </b-tabs>

    <!-- 나열 방식 -->
    <!-- <b-container>
        <b-row>
            <b-col cols="2">눈</b-col>
            <b-col cols="10">설명</b-col>
        </b-row>
    </b-container> -->
  </div>
</template>

<script>
export default {
  name: "FaceReadingDetail",
}
</script>


