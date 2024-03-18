import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()


for i in range(81):
    plt.subplot(9, 9, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.axis('off')
plt.show()

label_counts = np.bincount(y_train)

plt.pie(label_counts, labels=range(10))
plt.title('label counts')
plt.show()


X_train = X_train.astype(np.float32) / 255.0
X_test = X_test.astype(np.float32) / 255.0
model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=64)
loss, acc = model.evaluate(X_test, y_test)
print("深度学习精确度: ", acc)
