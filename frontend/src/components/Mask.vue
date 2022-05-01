<template>
  <div id="Mask">
    <el-dialog
      title="上传中"
      :visible.sync="dialogTableVisible"
      :show-close="false"
      :close-on-press-escape="false"
      :append-to-body="true"
      :close-on-click-modal="false"
      :center="true"
    >
      <el-progress :percentage="percentage"></el-progress>
      <span slot="footer" class="dialog-footer">请耐心等待</span>
    </el-dialog>

    <div id="CT">
      <div id="CT_image">
        <el-card
          id="CT_image_1"
          class="box-card"
          style="
            border-radius: 8px;
            width: 800px;
            height: 420px;
            margin-bottom: -30px;
          "
        >
          <div class="demo-image__preview1">
            <div
              v-loading="loading"
              element-loading-text="上传图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_1"
                class="image_1"
                :preview-src-list="srcList1"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">
                    
                  </div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 6px">原始图像</span>
            </div>
            <div class="img_info_1" style="border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton1"
                      type="primary"
                      icon="el-icon-upload"
                      class="download_bt"
                      v-on:click="true_upload"
                    >
                      上传图像
                      <input
                        ref="upload"
                        style="display: none"
                        name="file"
                        type="file"
                        @change="update($event, 1)"
                      />
                      <!-- 更改此处的change函数？ -->
                    </el-button>
            </div>
          </div>
          
          <div class="demo-image__preview1">
            <div
              v-loading="loading"
              element-loading-text="上传图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_2"
                class="image_1"
                :preview-src-list="srcList2"
                style="border-radius: 3px 3px 0 0"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">
                  </div>
                </div>
              </el-image>
            </div>
            <div class="img_info_1" style="border-radius: 0 0 5px 5px">
              <span style="color: white; letter-spacing: 4px">风格图像</span>
            </div>
            <div class="img_info_1" style="border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton2"
                      type="primary"
                      icon="el-icon-upload"
                      class="download_bt"
                      v-on:click="true_upload2"
                    >
                      上传图像
                      <input
                        ref="upload2"
                        style="display: none"
                        name="file"
                        type="file"
                        @change="update($event, 2)"
                      />
                      <!-- 更改此处的change函数？ -->
              </el-button>
            </div>
          </div>
        </el-card>
      </div>
      <div id="info_patient">
        <el-card class="box-card" style="border-radius: 8px; width: 800px;height:500px;">
          <el-tabs v-model="activeName">
            <el-tab-pane label="前景蒙版" name="first">
            </el-tab-pane>
            <el-tab-pane label="背景蒙版" name="second">
            </el-tab-pane>
            <el-tab-pane label="全参数" name="third">
            </el-tab-pane>

            <div v-if="activeName=='first'">
            <div class="demo-image__preview1" >
            <div
              v-loading="loading"
              element-loading-text="处理图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_3"
                class="image_2"
                :preview-src-list="srcList4"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">等待处理
                  </div>
                </div>
              </el-image>
              
              <div class="img_info_1" style="margin-top: 10px; border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton1"
                      type="primary"
                      class="download_bt"
                      @click="frontmask"
                    >开始处理
                </el-button>
                </div>
            </div>
            
            </div>
            <div class="demo-image__preview1" style="float:left;">
              <div class="param_block">
                <p>蒙版生成可能需要10秒左右，请您耐心等待。</p>
              </div>
              <div class="param_block">
                <span>选择图像</span>
              <el-radio-group style="margin-top: 10px;" v-model="isSrc">
                <el-radio :label="1">源图像</el-radio>
                <el-radio :label="0">风格图像</el-radio>
              </el-radio-group>
              </div>
              
              
            </div>
            </div>
            <div v-if="activeName=='second'">
            <div class="demo-image__preview1" >
            <div
              v-loading="loading"
              element-loading-text="处理图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_4"
                class="image_2"
                :preview-src-list="srcList4"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">等待处理
                  </div>
                </div>
              </el-image>
              
              <div class="img_info_1" style="margin-top: 10px; border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton1"
                      type="primary"
                      class="download_bt"
                      @click="backmask"
                    >开始处理
                </el-button>
                </div>
            </div>
            
            </div>
            <div class="demo-image__preview1" style="float:left;">
              <div class="param_block">
                <p>蒙版生成可能需要10秒左右，请您耐心等待。</p>
              </div>
              <div class="param_block">
                <span>选择图像</span>
              <el-radio-group style="margin-top: 10px;" v-model="isSrc">
                <el-radio :label="1">源图像</el-radio>
                <el-radio :label="0">风格图像</el-radio>
              </el-radio-group>
              </div>
              
              
            </div>
            </div>
            <div v-if="activeName=='third'">
            <div class="demo-image__preview1" >
            <div
              v-loading="loading"
              element-loading-text="处理图片中"
              element-loading-spinner="el-icon-loading"
            >
              <el-image
                :src="url_5"
                class="image_2"
                :preview-src-list="srcList4"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">等待处理
                  </div>
                </div>
              </el-image>
              
              <div class="img_info_1" style="margin-top: 10px; border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton1"
                      type="primary"
                      class="download_bt"
                      @click="automask"
                    >开始处理
                </el-button>
                </div>
            </div>
            
            </div>
            <div class="demo-image__preview1" style="float:left;">
              <div class="param_block">
                <p>蒙版生成可能需要10秒左右，请您耐心等待。</p>
              </div>
              <div class="param_block">
                <span>选择图像</span>
              <el-radio-group style="margin-top: 10px;" v-model="isSrc">
                <el-radio :label="1">源图像</el-radio>
                <el-radio :label="0">风格图像</el-radio>
              </el-radio-group>
              </div>
              <div class="param_block">
                <span>蒙版类型</span>
              <el-radio-group style="margin-top: 10px;" v-model="isBackground">
                <el-radio :label="1">背景蒙版</el-radio>
                <el-radio :label="0">前景蒙版</el-radio>
              </el-radio-group>
              </div>
              <div class="param_block">
                <span>算法模型</span>
              <el-radio-group style="margin-top: 10px;" v-model="mask_model">
                <el-radio label="u2netp">简易</el-radio>
                <el-radio label="u2net">完整</el-radio>
                <el-radio label="u2net_human_seg">人像</el-radio>
              </el-radio-group>
              </div>
              
            </div>
            </div>
            
            </el-tabs>

        </el-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Mask",
  data() {
    return {
      server_url: "http://127.0.0.1:5003",
      activeName: "first",
      active: 0,
      centerDialogVisible: true,
      url_1: "",  // 原始图片
      url_2: "",  // 风格图片
      url_3: "",  // 色域匹配结果
      url_4: "",  // 生成蒙版结果
      url_5: "",  // 生成蒙版结果
      textarea: "",
      srcList1: [],
      srcList2: [],
      srcList3: [],
      srcList4: [],
      srcList5: [],
      feature_list: [],
      feature_list_1: [],
      feat_list: [],
      url: "",
      visible: false,
      wait_return: "等待上传",
      wait_upload: "等待上传",
      loading: false,
      table: false,
      isNav: false,
      showbutton1: true,
      showbutton2: true,
      percentage: 0,
      fullscreenLoading: false,
      opacitys: {
        opacity: 0,
      },
      dialogTableVisible: false,

      // 蒙版参数
      isSrc: 1,
      isBackground: 1,
      // dilate: 1,
      mask_model: "u2netp",
    };
  },
  created: function () {
    document.title = "LearnableArt";
  },
  methods: {
    true_upload() {
      this.$refs.upload.click();
    },
    true_upload2() {
      this.$refs.upload2.click();
    },
    next() {
      this.active++;
    },
    // 获得目标文件
    getObjectURL(file) {
      var url = null;
      if (window.createObjcectURL != undefined) {
        url = window.createOjcectURL(file);
      } else if (window.URL != undefined) {
        url = window.URL.createObjectURL(file);
      } else if (window.webkitURL != undefined) {
        url = window.webkitURL.createObjectURL(file);
      }
      return url;
    },
    // 上传文件
    update(e, id) {
      // console.log(id);
      this.percentage = 0;
      this.dialogTableVisible = true;
      this.url_1 = "";
      this.url_2 = "";
      // this.srcList1 = [];
      // this.srcList2 = [];
      // console.log(this.srcList1);
      // console.log(this.srcList2);
      this.wait_return = "";
      this.wait_upload = "";
      this.feature_list = [];
      this.feat_list = [];
      this.fullscreenLoading = true;
      this.loading = true;
      this.showbutton = false;
      let file = e.target.files[0];
      if (id == 1) {
        this.url_1 = this.$options.methods.getObjectURL(file);
      } else if (id == 2) {
        this.url_2 = this.$options.methods.getObjectURL(file);
      }
      // this.url_1 = this.$options.methods.getObjectURL(file);
      let param = new FormData();               // 创建form对象
      param.append("file", file, file.name);    // 通过append向form对象添加数据
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };                                        // 添加请求头
      axios
        .post(this.server_url + "/upload", param, config)
        .then((response) => {
          this.percentage = 100;
          clearInterval(timer);
          if (id == 1) {
            this.url_1 = response.data.image_url;
            this.srcList1.push(this.url_1);
            this.url_2 = this.srcList2[this.srcList2.length-1];
          } else if (id == 2) {
            this.url_2 = response.data.draw_url;
            this.srcList2.push(this.url_2);
            this.url_1 = this.srcList1[this.srcList1.length-1];
          }

          this.fullscreenLoading = false;
          this.loading = false;

          // this.feat_list = Object.keys(response.data.image_info);

          // for (var i = 0; i < this.feat_list.length; i++) {
          //   response.data.image_info[this.feat_list[i]] = this.feat_list[i];
          //   this.feature_list.push(response.data.image_info[this.feat_list[i]]);
          // }

          // this.feature_list.push(response.data.image_info);
          // this.feature_list_1 = this.feature_list[0];
          this.dialogTableVisible = false;
          this.percentage = 0;
          this.notice("上传成功", "点击图片以查看大图", "success");
        });
    },
    // TODO: Real processing bar
    myFunc() {
      // A fake upload processing bar
      if (this.percentage + 33 < 99) {
        this.percentage = this.percentage + 33;
      } else {
        this.percentage = 99;
      }
    },
    drawChart() {},
    notice(str, msg, type) {
      this.$notify({
        title: str,
        message: msg,
        duration: 0,
        type: type,
      });
    },
    frontmask() {
      this.dialogTableVisible = true;
      this.percentage = 0;
      this.fullscreenLoading = true;
      this.loading = true;
      this.url_3 = "";
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      axios
        .get(this.server_url + "/automask", 
            {params: {src: this.srcList1[this.srcList1.length - 1], 
                      style: this.srcList2[this.srcList2.length - 1],
                      model: this.mask_model,
                      isSrc: this.isSrc,
                      isBackground: 0}})
        .then((response) => {
          this.percentage = 100;
          clearInterval(timer);
          if (response.data.status == 1) {
            this.url_3 = response.data.draw_url;
            this.srcList5.push(this.url_3);
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作完成", "点击图片以查看大图", "success");
          } else {
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作失败", "请重新检查", "error");
          }
          
        });
    },
    backmask() {
      this.dialogTableVisible = true;
      this.percentage = 0;
      this.fullscreenLoading = true;
      this.loading = true;
      this.url_4 = "";
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      axios
        .get(this.server_url + "/automask", 
            {params: {src: this.srcList1[this.srcList1.length - 1], 
                      style: this.srcList2[this.srcList2.length - 1],
                      model: this.mask_model,
                      isSrc: this.isSrc,
                      isBackground: 1}})
        .then((response) => {
          this.percentage = 100;
          clearInterval(timer);
          if (response.data.status == 1) {
            this.url_4 = response.data.draw_url;
            this.srcList4.push(this.url_4);
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作完成", "点击图片以查看大图", "success");
          } else {
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作失败", "请重新检查", "error");
          }
          
        });
    },
    automask() {
      this.dialogTableVisible = true;
      this.percentage = 0;
      this.fullscreenLoading = true;
      this.loading = true;
      this.url_5 = "";
      var timer = setInterval(() => {
        this.myFunc();
      }, 30);
      axios
        .get(this.server_url + "/automask", 
            {params: {src: this.srcList1[this.srcList1.length - 1], 
                      style: this.srcList2[this.srcList2.length - 1],
                      model: this.mask_model,
                      isSrc: this.isSrc,
                      isBackground: this.isBackground}})
        .then((response) => {
          this.percentage = 100;
          clearInterval(timer);
          if (response.data.status == 1) {
            this.url_5 = response.data.draw_url;
            this.srcList5.push(this.url_5);
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作完成", "点击图片以查看大图", "success");
          } else {
            this.fullscreenLoading = false;
            this.loading = false;

            this.dialogTableVisible = false;
            this.percentage = 0;
            this.notice("操作失败", "请重新检查", "error");
          }
          
        });
    },
  },
  mounted() {
    this.drawChart();
  },
};
</script>

<style>
.el-button {
  padding: 12px 20px !important;
}

#hello p {
  font-size: 15px !important;
  /*line-height: 25px;*/
}

.n1 .el-step__description {
  padding-right: 20%;
  font-size: 14px;
  line-height: 20px;
  /* font-weight: 400; */
}
</style>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  
}


.dialog_info {
  margin: 20px auto;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

.box-card {
  width: 680px;
  height: 200px;
  border-radius: 8px;
  margin-top: -20px;
}

#CT {
  display: flex;
  height: 100%;
  width: 80%;
  flex-wrap: wrap;
  justify-content: center;
  margin: 0 auto;
  margin-right: 0px;
  max-width: 1500px;
}

#CT_image_1 {
  width: 90%;
  height: 50%;
  margin: 0px auto;
  padding: 0px auto;
  margin-right: 180px;
  margin-bottom: 10px;
  border-radius: 4px;
}

#CT_image {
  margin-bottom: 10px;
  margin-left: 30px;
  margin-top: 5px;
}

.image_1 {
  width: 275px;
  height: 260px;
  background: #ffffff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.image_2 {
  width: 275px;
  height: 260px;
  background: #ffffff;
  /* display: inline-block; */
  /* float:left; */
}

.img_info_1 {
  height: 40px;
  width: 275px;
  margin-bottom: 10px;
  text-align: center;
  background-color: #21b3b9;
  line-height: 30px;
}

.demo-image__preview1 {
  width: 250px;
  height: 290px;
  margin: 20px 60px;
  float: left;
}

.demo-image__preview2 {
  width: 250px;
  height: 290px;

  margin: 20px 460px;
  /* background-color: green; */
}

.error {
  margin: 100px auto;
  width: 50%;
  padding: 10px;
  text-align: center;
}

.block-sidebar {
  position: fixed;
  display: none;
  left: 50%;
  margin-left: 600px;
  top: 350px;
  width: 60px;
  z-index: 99;
}

.block-sidebar .block-sidebar-item {
  font-size: 50px;
  color: lightblue;
  text-align: center;
  line-height: 50px;
  margin-bottom: 20px;
  cursor: pointer;
  display: block;
}

div {
  display: block;
}

.block-sidebar .block-sidebar-item:hover {
  color: #187aab;
}

.download_bt {
  padding: 10px 16px !important;
}

.handle_bt {
  padding: 10px 16px !important;
  text-align: center;
}

#upfile {
  width: 104px;
  height: 45px;
  background-color: #187aab;
  color: #fff;
  text-align: center;
  line-height: 45px;
  border-radius: 3px;
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.1), 0 2px 2px 0 rgba(0, 0, 0, 0.2);
  color: #fff;
  font-family: "Source Sans Pro", Verdana, sans-serif;
  font-size: 0.875rem;
}

.file {
  width: 200px;
  height: 130px;
  position: absolute;
  left: -20px;
  top: 0;
  z-index: 1;
  -moz-opacity: 0;
  -ms-opacity: 0;
  -webkit-opacity: 0;
  opacity: 0; /*css属性&mdash;&mdash;opcity不透明度，取值0-1*/
  filter: alpha(opacity=0);
  cursor: pointer;
}

#upload {
  position: relative;
  margin: 0px 0px;
}

#Mask {
  width: 85%;
  height: 800px;
  background-color: #ffffff;
  margin-left: 0px;
  display: flex;
  min-width: 1200px;

}

#info_patient {
  margin-top: 70px;
  margin-right: 150px;
  /* height: 4px; */
}

.param_block {
  margin-top: 20px;
  /* margin-bottom: 10px; */
  text-align: center;
  font-size: 14px;
}

.param_block span {
  font-size: 18px;
}

</style>


