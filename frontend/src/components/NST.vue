<template>
  <div id="NST">
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
        <el-card class="box-card" style="border-radius: 8px; width: 950px; height:550px;">
          <el-tabs v-model="activeName">
            <el-tab-pane label="简单迁移" name="first">
            </el-tab-pane>
            <el-tab-pane label="eee" name="second">
            </el-tab-pane>

            <div v-if="activeName=='first'">
            <div class="demo-image__preview1" style="float: left; width: 30%; margin: 50px 20px;">
            <!-- <div
              v-loading="loading"
              element-loading-text="处理图片中"
              element-loading-spinner="el-icon-loading"
            > -->
              <div>TEST：傻瓜风格迁移</div>
              <el-image
                :src="url_3"
                class="image_2"
                :preview-src-list="srcList3"
                style="border-radius: 3px"
              >
                <div slot="error">
                  <div slot="placeholder" class="error">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                  
                </div>
              </el-image>
              <!-- <el-progress :percentage="percentage"></el-progress> -->
              <!-- <div>请耐心等待</div> -->
              
              <div class="img_info_1" style="margin-top: 10px; border-radius: 5px; background-color: #ffffff">
              <el-button
                      v-show="showbutton1"
                      type="primary"
                      class="download_bt"
                      @click="nst"
                    >开始处理
                </el-button>
                </div>
            <!-- </div> -->
            </div>
            <div class="demo-image__preview1" style="float:left; width: 20%; margin: 10px;">
              <el-image
                :src="url_4_1"
                class="image_3"
                :preview-src-list="srcList4_1"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
              <el-image
                :src="url_4_2"
                class="image_3"
                :preview-src-list="srcList4_2"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
              <el-image
                :src="url_4_3"
                class="image_3"
                :preview-src-list="srcList4_3"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
            </div>
            <div class="demo-image__preview1" style="float:left; width: 20%; margin: 10px;">
              <el-image
                :src="url_4_4"
                class="image_3"
                :preview-src-list="srcList4_4"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
              <el-image
                :src="url_4_5"
                class="image_3"
                :preview-src-list="srcList4_5"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
              <el-image
                :src="url_4_6"
                class="image_3"
                :preview-src-list="srcList4_6"
                style="border-radius: 3px;"
              >
                <div slot="error">
                  <div slot="placeholder" class="error" style="margin-top: 50px;">
                    <el-progress :percentage="percentage"></el-progress>
                  </div>
                </div>
              </el-image>
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
                      @click="palettetransfer"
                    >开始处理
                </el-button>
                </div>
            </div>
            
            </div>
            <div class="demo-image__preview1" style="float:left;">
                <sketch-picker v-model="colors" />
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
import {Sketch} from "vue-color";

export default {
  name: "NST",
  components: {
    // 'photoshop-picker': Photoshop,
    'sketch-picker': Sketch,
  },
  data() {
    return {
      server_url: "http://127.0.0.1:5003",
      activeName: "first",
      active: 0,
      centerDialogVisible: true,
      url_1: "",  // 原始图片
      url_2: "",  // 风格图片
      url_3: "",  // 转换结果
      url_4_1: "",  // 过程图片
      url_4_2: "",
      url_4_3: "",
      url_4_4: "",
      url_4_5: "",
      url_4_6: "",
      textarea: "",
      srcList1: [],
      srcList2: [],
      srcList3: [],
      srcList4_1: [],
      srcList4_2: [],
      srcList4_3: [],
      srcList4_4: [],
      srcList4_5: [],
      srcList4_6: [],
      // feature_list: [],
      // feature_list_1: [],
      // feat_list: [],
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
      // 色彩迁移参数
      isMasked: 0,
      // algorithm: "fdm",
      match_mode: 0,
      // match_proportion: 1.0,

      // 调色盘
      colors : {
        hex: '#194d33',
        hex8: '#194D33A8',
        hsl: { h: 150, s: 0.5, l: 0.2, a: 1 },
        hsv: { h: 150, s: 0.66, v: 0.30, a: 1 },
        rgba: { r: 25, g: 77, b: 51, a: 1 },
        a: 1
      }
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
    dateFtt(fmt, date) 
    { 
      var o = { 
      "M+" : date.getMonth()+1,     //月份 
      "d+" : date.getDate(),     //日 
      "h+" : date.getHours(),     //小时 
      "m+" : date.getMinutes(),     //分 
      "s+" : date.getSeconds(),     //秒 
      "q+" : Math.floor((date.getMonth()+3)/3), //季度 
      "S" : date.getMilliseconds()    //毫秒 
      }; 
      if(/(y+)/.test(fmt)) 
      fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length)); 
      for(var k in o) 
      if(new RegExp("("+ k +")").test(fmt)) 
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length))); 
      return fmt; 
    },
    nst() {
      // console.log(this.srcList1[this.srcList1.length - 1]);
      // console.log(this.srcList2[this.srcList2.length - 1]);
      // this.dialogTableVisible = true;
      this.percentage = 0;
      // TODO: hash code for a certain pic
      var d = new Date();
      var timeString = this.dateFtt("yyyy-MM-dd-hh-mm-ss", d);
      // console.log(timeString);
      // this.fullscreenLoading = true;
      // this.loading = true;
      this.url_3 = "";

      // TEST: Get all tmp urls at first
      // var src_path = '.' + this.srcList1[this.srcList1.length - 1].substring(21);
      // var fname = src_path.substring(9).split('.')[0];
      // var ftype = src_path.substring(9).split('.')[1];
      // var tmp_path_1 = 'http://127.0.0.1:5003/tmp/draw/trans_' + timeString + '_' + fname + '_200.' + ftype;
      // var tmp_path_2 = 'http://127.0.0.1:5003/tmp/draw/trans_' + timeString + '_' + fname + '_400.' + ftype;
      // var tmp_path_3 = 'http://127.0.0.1:5003/tmp/draw/trans_' + timeString + '_' + fname + '_600.' + ftype;
      // var tmp_path_4 = 'http://127.0.0.1:5003/tmp/draw/trans_' + timeString + '_' + fname + '_800.' + ftype;
      // this.url_4_1 = tmp_path_1;
      // this.url_4_2 = tmp_path_2;
      // this.url_4_3 = tmp_path_3;
      // this.url_4_4 = tmp_path_4;
      // this.srcList4_1.push(this.url_4_1);
      // this.srcList4_2.push(this.url_4_2);
      // this.srcList4_3.push(this.url_4_3);
      // this.srcList4_4.push(this.url_4_4);

      var timer = setInterval(() => {
        this.myFunc();
        // TODO: get backend data
        $.ajax({
        url: "http://127.0.0.1:5003/nstjttmp",
        type: "GET",
        data: {'src':this.srcList1[this.srcList1.length - 1], 'timeString':timeString},
        dataType: "json",
        success: (data) => {
          if (data.tmp_url_1)   this.url_4_1 = data.tmp_url_1;
          if (data.tmp_url_2)   this.url_4_2 = data.tmp_url_2;
          if (data.tmp_url_3)   this.url_4_3 = data.tmp_url_3;
          if (data.tmp_url_4)   this.url_4_4 = data.tmp_url_4;

          this.srcList4_1.push(this.url_4_1);
          this.srcList4_2.push(this.url_4_2);
          this.srcList4_3.push(this.url_4_3);
          this.srcList4_4.push(this.url_4_4);
        }
      })
      }, 1000);
      axios
        .get(this.server_url + "/nstjt", 
            {params: {src: this.srcList1[this.srcList1.length - 1], 
                      ref: this.srcList2[this.srcList2.length - 1],
                      timeString: timeString}})
        .then((response) => {
          
          this.percentage = 100;
          clearInterval(timer);
          if (response.data.status == 1) {
            this.url_3 = response.data.draw_url;
            this.srcList3.push(this.url_3);
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
    palettetransfer() {
      this.dialogTableVisible = true;
      this.percentage = 0;
      this.fullscreenLoading = true;
      this.loading = true;
      this.url_4 = "";
      // console.log(this.colors);
      var timer = setInterval(() => {
      //   $.ajax({
      //   url: "/nstjt",
      //   type: "GET",
      //   data: senddata,
      //   dataType: "json",
      //   success: function (data) {
      //     console.log(data)
      //   }
      // })
      }, 1000);
      axios
        .get(this.server_url + "/colortransfer", 
            {params: {src: this.srcList1[this.srcList1.length - 1], 
                      ref: this.srcList2[this.srcList2.length - 1],
                      isMasked: this.isMasked,
                      hist_match: this.match_mode,}})
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

.divider {
  width: 50%;
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

.image_3 {
  width: 150px;
  height: 145px;
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
  width: 100%;
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

#NST {
  width: 85%;
  height: 800px;
  background-color: #ffffff;
  margin-left: 0px;
  display: flex;
  min-width: 1200px;

}

.divider {
  background-color: #eaeaea !important;
  height: 2px !important;
  width: 100%;
  margin-bottom: 50px;
}

.divider_1 {
  background-color: #ffffff;
  height: 2px !important;
  width: 100%;
  margin-bottom: 20px;
  margin: 20px auto;
}

.steps {
  font-family: "lucida grande", "lucida sans unicode", lucida, helvetica,
    "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
  color: #21b3b9;
  text-align: center;
  margin: 15px auto;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}

.step_1 {
  /*color: #303133 !important;*/
  margin: 20px 26px;
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


