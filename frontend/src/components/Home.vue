<template>
    <div id="home">
        这是一款面向艺术创作的完整图像风格迁移系统。<br>
        我们旨在通过最少的学习成本，提供最多的用户选择，获得最佳的图像质量。
        <el-image
          :src="require('../assets/20220426.jpg')"
          class="image_2"
          style="border-radius: 3px"
        ></el-image>
        <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 6px">系统流程示意</span>
            </div>
        Repository: TBA
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

.image_1 {
  width: 275px;
  height: 260px;
  background: #ffffff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.image_2 {
  width: 1100px;
  height: 600px;
  background: #ffffff;
  /* display: inline-block; */
  /* float:left; */
}

.img_info_1 {
  height: 40px;
  width: 1100px;
  margin-bottom: 10px;
  text-align: center;
  background-color: #21b3b9;
  line-height: 30px;
}

</style>