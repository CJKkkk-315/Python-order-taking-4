import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer, mean_squared_error, silhouette_score,accuracy_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV, StratifiedKFold
from sklearn.linear_model import LinearRegression, RidgeCV, SGDClassifier
from sklearn.ensemble import RandomForestRegressor

from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from tensorflow.keras.layers import Dense

seed=1220
np.random.seed(seed)

import warnings
warnings.filterwarnings('ignore')

train_test_split(random_state=)
a = RandomForestRegressor()
print(a.n_estimators)
RidgeCV