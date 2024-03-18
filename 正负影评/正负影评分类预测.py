from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')
def load_data_train(file_path):
    reviews = []
    labels = []
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            parts = line.strip().rsplit(' ', 1)
            review = parts[0]
            label = int(parts[1])
            reviews.append(review)
            labels.append(label)
    return reviews, labels

def load_data_test(file_path):
    reviews = []
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            parts = line.strip()
            reviews.append(parts)
    return reviews
train_X, train_y = load_data_train('data/rt-polarity.train')
test_X = load_data_test('data/rt-polarity.test')
dev_X, dev_y = load_data_train('data/rt-polarity.dev')

# 定义模型
models = {
    'LogisticRegression': LogisticRegression(),
    'SVC': SVC(),
    'MultinomialNB': MultinomialNB(),
    'RandomForestClassifier': RandomForestClassifier()
}

# 训练并验证每个模型
for name, model in models.items():
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        (name.lower(), model)
    ])

    pipeline.fit(train_X, train_y)
    predictions = pipeline.predict(dev_X)

    print(f"Model: {name}")
    print(classification_report(dev_y, predictions))

final_model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('NB', MultinomialNB())
    ])
final_model.fit(train_X + dev_X, train_y + dev_y)
test_predictions = final_model.predict(test_X)
for i in test_predictions:
    if i == 0:
        print(-1)
    else:
        print(1)
