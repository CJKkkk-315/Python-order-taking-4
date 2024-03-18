import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
f = open('D:/联想/2016全球幸福指数报告数据集.csv')
data_2016 = pd.read_csv(f)
happy_score = data_2016['Happiness Score']
x = data_2016['Economy (GDP per Capita)']
plt.scatter(x,happy_score)
plt.xlabel('Economy (GDP per Capita)')
plt.ylabel('Happiness Score')
plt.show()


x = data_2016['Health (Life Expectancy)']
plt.scatter(x,happy_score)
plt.xlabel('Health (Life Expectancy)')
plt.ylabel('Happiness Score')
plt.show()


x = data_2016['Freedom']
plt.scatter(x,happy_score)
plt.xlabel('Freedom')
plt.ylabel('Happiness Score')
plt.show()


x = data_2016['Trust (Government Corruption)']
plt.scatter(x,happy_score)
plt.xlabel('Trust (Government Corruption)')
plt.ylabel('Happiness Score')
plt.show()


x = data_2016['Generosity']
plt.scatter(x,happy_score)
plt.xlabel('Generosity')
plt.ylabel('Happiness Score')
plt.show()


x = data_2016['Dystopia Residual']
plt.scatter(x,happy_score)
plt.xlabel('Dystopia Residual')
plt.ylabel('Happiness Score')
plt.show()

x = data_2016['Family']
plt.scatter(x,happy_score)
plt.xlabel('Family')
plt.ylabel('Happiness Score')
plt.show()