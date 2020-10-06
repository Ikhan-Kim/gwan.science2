import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import FaceReading from "../views/FaceReading.vue";
import NameCompatibility from "@/views/NameCompatibility";
import FaceReadingResult from "@/views/FaceReadingResult";
import FaceReadingDetail from "@/views/FaceReadingDetail";
import NameCompatibilityResult from "@/views/NameCompatibilityResult";
import LifeClock from "@/views/LifeClock";
import LifeClockResult from "@/views/LifeClockResult";

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
    path: "/FaceReadingDetail",
    name: "FaceReadingDetail",
    component: FaceReadingDetail,
  },
  {
    path: "/NameCompatibility",
    name: "NameCompatibility",
    component: NameCompatibility,
  },
  {
    path:
      "/FaceReading/:eyebrowShape/:eyebrowInterval/:eyeSize/:eyeInterval/:eyeTail/:noseLength/:noseWidth/:mouthLength/:mouthThickness/:mouthTail",
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
  {
    path: "/LifeClock",
    name: "LifeClock",
    component: LifeClock,
  },
  {
    path: "/LifeClockResult/:age",
    name: "LifeClockResult",
    component: LifeClockResult,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
