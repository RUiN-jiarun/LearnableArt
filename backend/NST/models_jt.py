import jittor as jt
from jittor import init
from jittor import nn
import jittor

class VGG(nn.Module):

    def __init__(self, features, num_classes=1000):
        super(VGG, self).__init__()
        self.features = features
        # self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(4096, num_classes),
        )

def buildSequential(channel_list, pooling):
    layers = []
    in_channels = 3
    if pooling == 'max':
        pool2d = nn.MaxPool2d(kernel_size=2, stride=2)
    elif pooling == 'avg':
        pool2d = nn.AvgPool2d(kernel_size=2, stride=2)
    else:
        raise ValueError("Unrecognized pooling parameter")
    for c in channel_list:
        if c == 'P':
            layers += [pool2d]
        else:
            conv2d = nn.Conv(in_channels, c, kernel_size=3, padding=1)
            layers += [conv2d, nn.ReLU()]
            in_channels = c
    return nn.Sequential(*layers)


channel_list = {
'VGG-16p': [24, 22, 'P', 41, 51, 'P', 108, 89, 111, 'P', 184, 276, 228, 'P', 512, 512, 512, 'P'],
'VGG-16': [64, 64, 'P', 128, 128, 'P', 256, 256, 256, 'P', 512, 512, 512, 'P', 512, 512, 512, 'P'],
'VGG-19': [64, 64, 'P', 128, 128, 'P', 256, 256, 256, 256, 'P', 512, 512, 512, 512, 'P', 512, 512, 512, 512, 'P'],
}

vgg16_dict = {
'C': ['conv1_1', 'conv1_2', 'conv2_1', 'conv2_2', 'conv3_1', 'conv3_2', 'conv3_3', 'conv4_1', 'conv4_2', 'conv4_3', 'conv5_1', 'conv5_2', 'conv5_3'],
'R': ['relu1_1', 'relu1_2', 'relu2_1', 'relu2_2', 'relu3_1', 'relu3_2', 'relu3_3', 'relu4_1', 'relu4_2', 'relu4_3', 'relu5_1', 'relu5_2', 'relu5_3'],
'P': ['pool1', 'pool2', 'pool3', 'pool4', 'pool5'],
}
vgg19_dict = {
'C': ['conv1_1', 'conv1_2', 'conv2_1', 'conv2_2', 'conv3_1', 'conv3_2', 'conv3_3', 'conv3_4', 'conv4_1', 'conv4_2', 'conv4_3', 'conv4_4', 'conv5_1', 'conv5_2', 'conv5_3', 'conv5_4'],
'R': ['relu1_1', 'relu1_2', 'relu2_1', 'relu2_2', 'relu3_1', 'relu3_2', 'relu3_3', 'relu3_4', 'relu4_1', 'relu4_2', 'relu4_3', 'relu4_4', 'relu5_1', 'relu5_2', 'relu5_3', 'relu5_4'],
'P': ['pool1', 'pool2', 'pool3', 'pool4', 'pool5'],
}

def modelSelector(model_file, pooling):
    if "19" in model_file:
        print("VGG-19 Architecture Detected")
        cnn, layerList = VGG(buildSequential(channel_list['VGG-19'], pooling)), vgg19_dict
    elif "16" in model_file:
        print("VGG-16 Architecture Detected")
        cnn, layerList = VGG(buildSequential(channel_list['VGG-16'], pooling)), vgg16_dict
    return cnn, layerList

# Print like Torch7/loadcaffe
def print_model(cnn, layerList):
    c = 0
    for l in list(cnn):
        if "Conv" in str(l):
            s = str(l)[5:]
            in_c = s.split(', ')[0]
            out_c = s.split(', ')[1]
            kernel_size = s.split(', (')[1].split(')')[0]
            # print(in_c, out_c, kernel_size)
            # in_c, out_c, ks  = str(l.in_channels), str(l.out_channels), str(l.kernel_size)
            print(layerList['C'][c] +": " +  (out_c + " " + in_c + " " + kernel_size).replace(")",'').replace("(",'').replace(",",'') )
            c+=1
        if c == len(layerList['C']):
            break

# Load the model, and configure pooling layer type
def loadModel(model_file, pooling, use_gpu):
    cnn, layerList = modelSelector(str(model_file).lower(), pooling)

    cnn.load_state_dict(jittor.load(model_file))
    print("Successfully loaded " + str(model_file))

    # Maybe convert the model to cuda now, to avoid later issues
    # if "c" not in str(use_gpu).lower() or "c" not in str(use_gpu[0]).lower():
    #     cnn = cnn.cuda()
    
    cnn = cnn.features
    # print(list(cnn)[0])
    print_model(cnn, layerList)

    return cnn, layerList

if __name__ == '__main__':
    loadModel('models/vgg19.pkl', 'max', use_gpu='cuda:0')
