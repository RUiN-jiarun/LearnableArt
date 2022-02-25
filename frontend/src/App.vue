<template>
  <div id="app">
    <app-home></app-home>
    <app-header></app-header>
    
    <app-content></app-content>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Content from "./components/Content";
import Home from "./components/Home";
export default {
  name: "rua",
  data() {
    return {};
  },
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-content": Content,
    "app-home": Home,
  },
  methods: {},
};
</script>

<style scope="this api replaced by slot-scope in 2.5.0+">
</style>
