import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D, LSTM, Bidirectional, Attention, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# 加载数据集
df = pd.read_csv('data3.csv')
X = df[['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']]
y = df['lable']

# 标准化和编码
scaler = StandardScaler()
X = scaler.fit_transform(X)

encoder = LabelEncoder()
y = encoder.fit_transform(y)

# 转化为需要的形状
X = np.reshape(X, (X.shape[0], X.shape[1], 1))
y = to_categorical(y)

# 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


input_layer = Input(shape=(X.shape[1], 1))
bidirectional_lstm = Bidirectional(LSTM(64, return_sequences=False))(input_layer)
dropout = Dropout(0.5)(bidirectional_lstm)
output_layer = Dense(y.shape[1], activation='softmax')(dropout)

model = Model(inputs=input_layer, outputs=output_layer)

# 编译和训练模型
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_split=0.2, batch_size=32)


# 编译和训练模型
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

import matplotlib.pyplot as plt

# 训练模型并保存历史数据
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2, batch_size=32)

# 绘制训练 & 验证的损失值
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# 在训练集和测试集上进行预测
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)
y_test = np.argmax(y_test, axis=1)
y_train = np.argmax(y_train, axis=1)
train_pred = np.argmax(train_pred, axis=1)
test_pred = np.argmax(test_pred, axis=1)
print('accuracy:',accuracy_score(y_test,test_pred))
print('precision:',precision_score(y_test,test_pred,average='macro'))
print('recall:',recall_score(y_test,test_pred,average='macro'))
print('f1:',f1_score(y_test,test_pred,average='macro'))
# 绘制训练集的真实值与预测值
plt.figure(figsize=(12, 6))
plt.plot(y_train)
plt.plot(train_pred)
plt.title('Train Value vs Prediction')
plt.ylabel('Value')
plt.xlabel('Data Point Index')
plt.legend(['True Value', 'Predicted Value'], loc='upper left')
plt.show()

# 绘制测试集的真实值与预测值
plt.figure(figsize=(12, 6))
plt.plot(y_test)
plt.plot(test_pred)
plt.title('Test Value vs Prediction')
plt.ylabel('Value')
plt.xlabel('Data Point Index')
plt.legend(['True Value', 'Predicted Value'], loc='upper left')
plt.show()

