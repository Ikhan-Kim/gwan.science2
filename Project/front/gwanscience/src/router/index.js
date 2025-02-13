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
import Builders from "@/views/Builders";

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
    path:
      "/FaceReadingDetail/:eyebrowInterval/:eyeSize/:eyeInterval/:eyeTail/:noseLength/:noseWidth/:mouthLength/:mouthThickness/:mouthTail",
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
      "/FaceReading/:username/:eyebrowInterval/:eyeSize/:eyeInterval/:eyeTail/:noseLength/:noseWidth/:mouthLength/:mouthThickness/:mouthTail",
    name: "FaceReadingResult",
    component: FaceReadingResult,
    props: true,
  },
  {
    path: "/NameCompatibilityResult/:name1/:name2",
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
  {
    path: "/Builders",
    name: "Builders",
    component: Builders,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
