import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import FaceReading from "../views/FaceReading.vue";
import inputName from "@/views/inputName";
import result from "@/views/result";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/face-reading",
    name: "FaceReading",
    component: FaceReading,
  },
  {
    path: "/inputName",
    name: "inputName",
    component: inputName,
  },
  {
    path: "/result",
    name: "result",
    component: result,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
