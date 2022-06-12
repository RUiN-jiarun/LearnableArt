# 前端说明

## 组件功能

主要实现的模组在`src/components`里，路由配置在`main.js`中。

* `App.vue`：框架与导航栏
* `Content.vue`：预处理的色域匹配部分
* `Cut.vue`：后处理的蒙版裁切部分
* `Footer.vue`：Footer
* `Header.vue`：Header
* `Home.vue`：首页
* `Mask.vue`：预处理的自动蒙版部分
* `NSTjt.vue`：jittor框架的风格迁移——并不是很完整
* `NSTpt.vue`：pytorch框架的风格迁移——主要部分
* `Optim.vue`：后处理的色彩迁移部分
* `SR.vue`：后处理的超分辨率部分

## 基本变量

在每个组件所在的vue文件的data域段可以看到几个字符串和对应的list：

<img src="https://ruin-typora.oss-cn-beijing.aliyuncs.com/image-20220612103308989.png" alt="image-20220612103308989" style="zoom:67%;" />

其中url字段是用于存储中间图片url并传给服务器，srcList用于存储一系列用于预览的图片url

在NSTpt.vue里写了一段非常丑陋的假进度条……就是那两个`progress()`函数