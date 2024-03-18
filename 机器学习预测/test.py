import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
seed=0 # use this random seed throughout your code
# Load the data and take a sneak peek using "head" or "tail" method
data = pd.read_csv('Real_estate_valuation_dataset.csv')
# data.head()
# Use "hist" to plot the distribution of the data, using an appropriate bin size:
# data.hist(bins=12)
# Compute the standard correlation coefficient between every pair of attributes:
corr_matrix = data.corr()
# Read the corresponding column
y = data['distance_to_the_nearest_MRT_station']
x = data['house_price_of_unit_area']

# transform x into a design matrix
one = np.ones(x.size)
x  = np.c_[one,x]

# Split the data into training and test set with 20% test size and random_state=seed
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2,random_state=seed)

# Because the values of features vary in magnitude, we often
# standardize features by removing the mean and scaling to unit
# variance using sklearn.preprocessing.StandardScaler
std = StandardScaler()
xtrain = std.fit_transform(xtrain)
xtest = std.fit_transform(xtest)
# Define the model
model = LogisticRegression()

# Fit the model using the training set

model.fit(xtrain,ytrain)

# Obtain intercept and coefficient
intercept = model.intercept_
coefficient = model.coef_
print("Intercept is:", intercept.round(3))
print("Coefficient are:", coefficient.round(3))

# Obtain coefficient of determination (R-squared) on the training data
r2_train = r2_score(y_true=ytrain,y_pred=model.predict(xtrain))
print("Coefficient of determination on the training set: %.3f" % r2_train)

# Make predictions using the testing set
ypred = model.predict_proba()

# Evaluate performance on the test data
r2_test = r2_score(y_true=ytest,y_pred=ypred)
print("Coefficient of determination on the test set: %.3f" % r2_test)

xplot = [i for i in range(len(ypred))]
y1 = ypred
y2 = ytest
plt.plot(xplot,y1)
plt.plot(xplot,y2)
plt.legend(["predicted", "test"])
plt.show()
model = SGDRegressor(alpha=0.01)