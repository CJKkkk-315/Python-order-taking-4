from sklearn.tree import DecisionTreeClassifier
train = open('data_train.txt')
train = train.read()
train = train.split('\n')
train = [i.split() for i in train][:-1]
train_X = [list(map(float,i[:-1])) for i in train]
train_y = [float(i[-1]) for i in train]

test = open('data_test.txt')
test = test.read()
test = test.split('\n')
test = [i.split() for i in test]
test = [list(map(float,i)) for i in test][:-1]
print(len(test))
model = DecisionTreeClassifier()
model.fit(train_X,train_y)
pred = list(model.predict(test))
with open('model.txt','w') as f:
    for i in pred:
        f.write(str(int(i)) + '\n')