# 后端说明

## 组件功能

* `automask`：基于U2-Net的自动前背景分离
* `postprocessing`：几个简单的色彩迁移工具
* `preprocessing`：基于两种图像统计数据匹配的色域匹配方法，一个是FDM，一个是HM
* `srgan`：基于SRGAN的超分辨率工具
* `tmp`：在后端部署时自动生成，用于存放图片。因为没有使用数据库，都是本地存储
* `app.py`：Flask编写的服务器端

## 服务器部署文件

```sh
$ python app.py
```

每一个路由对应前端页面，都使用了GET方法而不是POST，除了上传文件。使用GET，从前端传回的数据中读取图片的url。当然，前端的url和后端上传后的url不一样，这里用了非常暴力的方法来修改：

![image-20220612105247889](https://ruin-typora.oss-cn-beijing.aliyuncs.com/image-20220612105247889.png)

这个21是因为本地路径都是`http://127.0.0.1:5003/xxxxx`，就删去了前面的部分，改成了相对路径。如果部署到其他服务器上，需要修改这一部分

返回数据使用`jsonify()`返回一个字典，传入要显示的新的图片的路径。

## NST部分

详见NST文件里的README.md