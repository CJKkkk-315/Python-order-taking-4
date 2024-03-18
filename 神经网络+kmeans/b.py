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
minibatch_size = 20
learning_rates = [0.001, 0.1, 1.0, 10, 100]

# 为每个学习率创建一个 MLP 分类器并进行训练
for learning_rate in learning_rates:
    print(f'Training with learning rate: {learning_rate}')

    mlp = MLPClassifier(hidden_layer_sizes=layer_sizes[1:],
                        batch_size=minibatch_size,
                        max_iter=epochs,
                        learning_rate_init=learning_rate,
                        solver='sgd')

    # 存储每个epoch的准确率
    accuracies = []

    # 训练模型并记录每个epoch的准确率
    for epoch in range(epochs):
        mlp.partial_fit(train_X, train_y, classes=np.unique(train_y))
        y_pred = mlp.predict(test_X)
        accuracy = accuracy_score(test_y, y_pred)
        accuracies.append(accuracy)
        print(f'Epoch {epoch + 1}/{epochs}, Accuracy: {accuracy:.4f}')

    # 画出准确率与 epoch 的关系
    plt.plot(range(1, epochs + 1), accuracies, label=f'LR = {learning_rate}')

plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Epoch for Different Learning Rates')
plt.legend()
plt.grid()
plt.show()
