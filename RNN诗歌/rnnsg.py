data_path = "poetry.txt"
forbidden_chars = ['（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']']
vocab_size = 3000
unknown_char = " "
train_num = 6
poems = []
all_chars = []

with open(data_path, encoding="utf-8") as f:
    for line in f:
        poem = line.split(":")[1].replace(" ", "")
        flag = True
        for forbidden_char in forbidden_chars:
            if forbidden_char in poem:
                flag = False
                break
        if len(poem) < 12 or poem[5] != '，' or (len(poem) - 1) % 6 != 0:
            flag = False

        if flag:
            for char in poem:
                all_chars.append(char)
            poems.append(poem)

from collections import Counter
counter = Counter(all_chars)
char_counts = sorted(counter.items(), key=lambda x: -x[1])
most_common_chars, _ = zip(*char_counts)
used_chars = most_common_chars[:vocab_size - 1] + (unknown_char,)
char_to_id = {char: index for index, char in enumerate(used_chars)}
id_to_char = {index: char for index, char in enumerate(used_chars)}

import numpy as np

def char_to_one_hot(char):
    one_hot_char = np.zeros(vocab_size)
    if char not in char_to_id.keys():
        char = unknown_char
    index = char_to_id[char]
    one_hot_char[index] = 1
    return one_hot_char

def poem_to_one_hot(poem):
    one_hot_poem = []
    for char in poem:
        one_hot_poem.append(char_to_one_hot(char))
    return one_hot_poem

X_train = []
Y_train = []

for poem in poems:
    for i in range(len(poem)):
        X = poem[i:i+train_num]
        Y = poem[i+train_num]
        if "\n" not in X and "\n" not in Y:
            X_train.append(X)
            Y_train.append(Y)
        else:
            break

from keras.callbacks import LambdaCallback,ModelCheckpoint
from keras.models import Input, Model
from keras.layers import Dropout, Dense,SimpleRNN
from keras.optimizers import Adam

def build_model():
    print('building model')
    input_tensor = Input(shape=(train_num, vocab_size))
    rnn = SimpleRNN(512, return_sequences=True)(input_tensor)
    dropout = Dropout(0.6)(rnn)

    rnn = SimpleRNN(256)(dropout)
    dropout = Dropout(0.6)(rnn)
    dense = Dense(vocab_size, activation='softmax')(dropout)

    model = Model(inputs=input_tensor, outputs=dense)
    optimizer = Adam(lr=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    model.summary()
    return model

model = build_model()

def predict_next(x):
    predict_y = model.predict(x)[0]
    index = np.argmax(predict_y)
    return index

def generate_sample_result(epoch, logs):
    if epoch % 1 == 0:
        predict_sentence = "一朝春夏改，"
        predict_data = predict_sentence
        while len(predict_sentence) < 24:
            X_data = np.array(poem_to_one_hot(predict_data)).reshape(1, train_num, vocab_size)
            y = predict_next(X_data)
            predict_sentence = predict_sentence + id_to_char[y]
            predict_data = predict_data[1:] + id_to_char[y]
        with open('out/out.txt', 'a', encoding='utf-8') as f:
            f.write(predict_data+'\n')

import math

def get_batch(batch_size=32):
    steps = math.ceil(len(X_train) / batch_size)
    while True:
        for i in range(steps):
            X_train_batch = []
            Y_train_batch = []
            X_batch_data = X_train[i * batch_size: (i + 1) * batch_size]
            Y_batch_data = Y_train[i * batch_size: (i + 1) * batch_size]

            for x, y in zip(X_batch_data, Y_batch_data):
                X_train_batch.append(poem_to_one_hot(x))
                Y_train_batch.append(char_to_one_hot(y))
            yield np.array(X_train_batch), np.array(Y_train_batch)

batch_size = 2048

model.fit_generator(
    generator=get_batch(batch_size),
    verbose=True,
    steps_per_epoch=math.ceil(len(X_train) / batch_size),
    epochs=1000000,
    callbacks=[
        ModelCheckpoint("poetry_model.hdf5", verbose=1, monitor='val_loss', period=1),
        LambdaCallback(on_epoch_end=generate_sample_result)
    ]
)
