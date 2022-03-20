<template>
  <div class="sidebar" style="">
      
      <el-row style="height: 100%; overflow:hidden; display:flex;">
        <el-col style="min-height: 100%;background-color: #21b3b9;overflow: hidden;width:15%">
          <el-menu
            router
            :default-active="$route.name"
            class="el-menu-horizontal-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="#21b3b9"
            text-color="#bfcbd9"
            active-text-color="#049eff">
            <el-menu-item index="/"><i class="el-icon-menu"></i>首页</el-menu-item>
            <el-submenu index="pre">
              <template slot="title"><i class="el-icon-document"></i>预处理</template>
              <el-menu-item index="match">色域匹配</el-menu-item>
              <el-menu-item index="mask">智能蒙版</el-menu-item>
            </el-submenu>
             
            
            <el-submenu index="3">
              <template slot="title"><i class="el-icon-document"></i>编辑</template>
              <el-menu-item index="index">编辑1</el-menu-item>
              <el-menu-item index="index2">编辑2</el-menu-item>
              <el-menu-item index="index3">编辑3</el-menu-item>
            </el-submenu>
            <el-menu-item index="post"><i class="el-icon-document"></i>后处理</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="150">
          <app-header></app-header>
          <keep-alive>
            
            <router-view></router-view>
          </keep-alive>
          <app-footer></app-footer>
        </el-col>
        <!-- <router-view></router-view> -->
      </el-row>

  </div>
</template>

<script>
import Header from "./Header";
import Footer from "./Footer";
export default {
  name: 'App',
  computed: {
    /*defaultActive: function () {
      /!*刷新后导航还是高亮显示且展开*!/ //或者直接$route.name
      //console.log(this.$route.path) /home/list  只取list就行 和el-menu-item的index对应
      return this.$route.path.replace('/home/', '');
    }*/
  },
  data() {
    return {}
  },
  mounted() {},
  components: {
    "app-header": Header,
    "app-footer": Footer,
  },
  methods: {
    handleOpen(key, keyPath) {
      // console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      // console.log(key, keyPath);
    },
  }
}
</script>
<style lang="less" scoped>
.sidebar, .fillcontain {
  height: 100%;
}

.el-menu {
  border: 0;
}
.el-col {
  background-color: #ffffff;
  height: 100%;
  overflow: auto;
}
.sidebar {
  display: block;
  position: relative;
  // overflow-y: scroll;
  /deep/ .el-submenu .el-menu-item {
    background-color: #1f2d3d !important;
  }
  /deep/ .el-submenu__title:hover, .el-submenu .el-menu-item:hover {
    background-color: #48576a !important;
  }
}
</style>
