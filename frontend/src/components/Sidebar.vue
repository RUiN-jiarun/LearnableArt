<template>
  <div class="sidebar" style="position:fixed">
    <div class="manage_page fillcontain">
      <el-row style="height: 100%;width:150px;overflow:hidden;display:flex;">
        <el-col :span="3" style="min-height: 100%;background-color: #21b3b9;overflow: hidden;width:100%">
          <el-menu
            router
            :default-active="$route.name"
            class="el-menu-horizontal-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="#21b3b9"
            text-color="#bfcbd9"
            active-text-color="#049eff">
            <el-menu-item index="home"><i class="el-icon-menu"></i>首页</el-menu-item>
            <el-menu-item index="pre"><i class="el-icon-document"></i>预处理</el-menu-item>
             
            
            <el-submenu index="3">
              <template slot="title"><i class="el-icon-document"></i>编辑</template>
              <el-menu-item index="index">编辑1</el-menu-item>
              <el-menu-item index="index2">编辑2</el-menu-item>
              <el-menu-item index="index3">编辑3</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-col>
        <el-col :span="0">
          <keep-alive>
            <router-view></router-view>
          </keep-alive>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Sidebar',
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
  methods: {
    handleOpen(key, keyPath) {
    },
    handleClose(key, keyPath) {
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
  background-color: #21b3b9;
  height: 100%;
  overflow: auto;
}
.sidebar {
  /deep/ .el-submenu .el-menu-item {
    background-color: #1f2d3d !important;
  }
  /deep/ .el-submenu__title:hover, .el-submenu .el-menu-item:hover {
    background-color: #48576a !important;
  }
}
</style>
