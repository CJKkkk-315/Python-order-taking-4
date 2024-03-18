import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# 加载数据集
def load_dataset(feature_file, label_file):
    X = np.loadtxt(feature_file, delimiter=',')
    y = np.loadtxt(label_file, delimiter=',')
    return X, y


# 读取训练集和测试集
train_X, train_y = load_dataset('TrainDigitX.csv.gz', 'TrainDigitY.csv.gz')
test_X, test_y = load_dataset('TestDigitX.csv.gz', 'TestDigitY.csv.gz')

# 定义神经网络结构和参数
layer_sizes = [784, 30, 10]
epochs = 30
learning_rate = 3.0
minibatch_sizes = [1, 5, 10, 20, 100]

# 存储不同mini-batch大小的最终测试精度
final_accuracies = []

# 为每个mini-batch大小创建一个 MLP 分类器并进行训练
for minibatch_size in minibatch_sizes:
    print(f'Training with mini-batch size: {minibatch_size}')

    mlp = MLPClassifier(hidden_layer_sizes=layer_sizes[1:],
                        batch_size=minibatch_size,
                        max_iter=epochs,
                        learning_rate_init=learning_rate,
                        solver='sgd')

    # 训练模型
    mlp.fit(train_X, train_y)

    # 计算最终测试精度
    y_pred = mlp.predict(test_X)
    final_accuracy = accuracy_score(test_y, y_pred)
    final_accuracies.append(final_accuracy)
    print(f'Mini-batch size: {minibatch_size}, Final Accuracy: {final_accuracy:.4f}')

# 画出最终测试精度与 mini-batch 的关系
plt.plot(minibatch_sizes, final_accuracies, marker='o')
plt.xlabel('Mini-batch Size')
plt.ylabel('Final Accuracy')
plt.title('Final Accuracy vs. Mini-batch Size')
plt.grid()
plt.show()
