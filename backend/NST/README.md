# NST

Pytorch version adapted from [ProGamerGov/neural-style-pt: PyTorch implementation of neural style transfer algorithm (github.com)](https://github.com/ProGamerGov/neural-style-pt) with some improvement:

* All layers selected.
* Shifted-activation Gram matrix.
* Transformed feature maps.

usage:

```sh
$ python neural_style.py -style_image <image.jpg> -content_image <image.jpg>
```

or

```sh
$ python neural_style.py -style_image examples/inputs/bird.png -content_image examples/inputs/starry_night.jpg -output_image out.png -model_file models/vgg19-d01eb7cb.pth -gpu 0 -backend cudnn -num_iterations 1000 -image_size 800 -optimizer lfbgs -improve_gram
```

![out](https://ruin-typora.oss-cn-beijing.aliyuncs.com/out.png)

Jittor version created according to the Pytorch version.

To install jittor, please follow [安装 — Jittor (tsinghua.edu.cn)](https://cg.cs.tsinghua.edu.cn/jittor/download/).

For evaluation metrics please check `eval` folder. The results folders are removed for large size.



## TODO

Jittor version **DID NOT** imply the lbfgs optimizer. `lbfgs_jt.py` is a temp file.

