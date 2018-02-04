
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model

from sklearn.linear_model import LinearRegression


# In[2]:
listt = []
years = []
data = pd.read_csv('datasets/bank/API_FR.INR.LEND_DS2_en_csv_v2.csv')
data = np.array(data)
x = data[107:108,22:39].T
y = []
print(len(x))
start = 2001
for i in range(len(x)):
    y.append(start+i)

linreg = LinearRegression().fit(x, y)

for x in range(2020,2021):
    years.append(x)
    listt.append(linreg.predict(x))

print(listt)

plt.scatter(years, listt, c='r')
plt.show()
# In[ ]:



