import keras
from keras import models
from keras import layers
from keras import optimizers
import matplotlib.pyplot as plt
import numpy as np
import pickle  #加载cifar格式的数据
from sklearn.preprocessing import Normalizer

def normalization(data):
    for j in range(data.shape[1]):
        feature = data[:,j]
        ma = max(feature)
        mi = min(feature)
        denominator = max(ma-mi,1)
        for i in range(data.shape[0]):
            data[i][j] = -1 + 2 * (data[i][j])/denominator
    return data


def PrepareDataset(file_path): #准备Cifar训练集与测试集
    binary_data = open(file_path, 'rb')
    dict = pickle.load(binary_data,encoding='bytes')
    print("读取的dict数据的键:",dict.keys())
    print("示例，前十个数据的标签： ",dict[b'labels'][0:10])
    cifar_data = dict[b'data']
    #cifar_data = np.reshape(dict[b'data'],[-1,3,32,32])  将数据转换成32*32形式，用于卷积神经网络，作业1为常规的神经网络
    cifar_label = dict[b'labels']
    print("转化为nparray的数据的维度：", cifar_data.shape)
    return cifar_data,cifar_label

def show(data,i=0): #可视化，展示给定索引的对应图片
    pic = np.reshape(data[i],[3,32,32])
    pic = np.transpose(pic,(1,2,0))
    plt.rcParams['figure.figsize']=(3.2, 3.2)
    plt.imshow(pic)
    plt.show()

# cifar中包含的图片所属的类别，对应读取的dict数据中的b labels的0-9
classes=('plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck')
#输入：特征、标签
#输出：过滤后的特征、标签
#内容：将输入数据中标签为猫和狗的特征以及标签，以list形式输出，特征数据值不发生变化，标签数据猫对应的值需变为0，狗变为1
def filter_data(data,label):

    return X,Y

#输入，训练数据
#输出，训练好的模型
#内容：构建一个不少于三层的神经网络模型，并用输入数据进行训练，然后输出,训练次数（epoch）需设置为10
#激活函数备选值: relu sigmoid softmax softplus tanh exponential
def train_model(X,Y):

    return model


if __name__ == "__main__":
    data,label = PrepareDataset('data_batch_1')
    print(data)
    print(label)
    exit(0)
    X,Y = filter_data(data,label)
    #X = normalization(X) 完成第一轮测试以后，试着加入本行代码，再次进行测试
    training_label = Y[0:-100]
    training_data = X[0:-100]
    test_label = Y[-100:]
    test_data = X[-100:]
    print(training_label)
    print(training_label.shape,training_data.shape,test_label.shape,test_data.shape)
    model = train_model(training_data,training_label)
    print(np.argmax(model.predict(test_data),axis=1))
    model.evaluate(X,Y)
    #show(data)