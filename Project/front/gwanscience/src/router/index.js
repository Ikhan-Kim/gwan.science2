import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import FaceReading from "../views/FaceReading.vue";
import NameCompatibility from "@/views/NameCompatibility";
import FaceReadingResult from "@/views/FaceReadingResult";
import NameCompatibilityResult from "@/views/NameCompatibilityResult";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/FaceReading",
    name: "FaceReading",
    component: FaceReading,
  },
  {
    path: "/NameCompatibility",
    name: "NameCompatibility",
    component: NameCompatibility,
  },
  {
    path: "/FaceReading/result",
    name: "FaceReadingResult",
    component: FaceReadingResult,
    props: true,
  },
  {
    path: "/NameCompatibility/:name1/:name2",
    name: "NameCompatibilityResult",
    component: NameCompatibilityResult,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
