import pandas as pd
import numpy as np
data = pd.read_csv('data_6.csv')
data.columns = [i.split(':')[1] for i in data.columns]