<template>
  <div id="app">
    <app-sidebar></app-sidebar>
    <app-header></app-header>
    <router-view></router-view>
    <!-- <app-content></app-content> -->
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
// import Content from "./components/Content";
import Sidebar from "./components/Sidebar";
export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    "app-header": Header,
    "app-footer": Footer,
    // "app-content": Content,
    "app-sidebar": Sidebar,
  },
  methods: {},
};
</script>

<style scope="this api replaced by slot-scope in 2.5.0+">
</style>
