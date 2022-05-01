<template>
    <div id="home">
        这是一款面向艺术创作的完整图像风格迁移系统。
    </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {}
  },
  mounted() {},
  created: function () {
    document.title = "LearnableArt";
  },
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

div {
  display: block;
}

#home {
  width: 100%;
  /* height: 100%; */
  background-color: #ffffff;
  margin-left: 100px;
  /* display: flex; */
  min-width: 1300px;

}

</style>