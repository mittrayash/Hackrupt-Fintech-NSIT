
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model


# In[3]:

df = pd.read_csv('datasets/bank/API_FR.INR.LEND_DS2_en_csv_v2.csv')


# In[4]:

df = df[df['Country Name'] == 'India']


# In[5]:

df = df[df.columns[-30:-2]]


# In[6]:

df


# In[7]:

df2 = pd.DataFrame()  
df2['Year'] = df.columns
df2['Price'] = df.values.reshape(-1)


# In[57]:

df2


# In[58]:

fig = plt.figure(1)
axes = fig.add_subplot(111)
axes.plot(df2['Year'], df2['Price'])


# In[59]:

lss = []

for x in range(len(df2['Year']) - 1):
    lss.append(df2['Price'][x+1] - df2['Price'][x])
print(lss)
lss.append(lss[-1])


# In[60]:

df2['Slope'] = lss


# In[61]:

df2


# In[62]:

df2 = df2[['Year', 'Slope', 'Price']]


# In[63]:

df2


# In[64]:

from sklearn.linear_model import LinearRegression

linreg = LinearRegression().fit(df2[df2.columns[0:1]], df2['Price'])


# In[65]:

print('linear model coeff (w): {}'.format(linreg.coef_))
print('linear model intercept (b): {:.3f}'.format(linreg.intercept_))


# In[66]:

listt = []
years = []
for x in range(2020,2021):
    years.append(x)
    listt.append(linreg.predict(x))
listt

plt.scatter(years, listt, c='r')


# In[67]:



# In[68]:


plt.show()


# In[ ]:



