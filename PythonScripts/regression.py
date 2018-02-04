
# coding: utf-8

# In[181]:

import sklearn.linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[253]:

df = pd.read_csv(os.path.dirname(os.path.dirname(__file__)) + '/dataset.csv')
df = df.drop('Unnamed: 0',1)
df.head()

df.head(10)


# In[276]:

def par(idd, df):
    y = df[df['ID'] == idd]['final'].values
    lis = []
    bias = 1000000
    x = 0
    for i in y:
        if(i > 0):
            x = bias / (1 + np.e**(-i))
            # x = bias* (4*i**(1/2) + 4*i + 1)
            lis.append(x)
        else:
            lis.append(0)
    return lis


            
# lis = par(df['final'])


# In[277]:




# In[296]:

lll = []
mmm = []
def calculator(idd, temp_sum):
    global lll, mmm

    from sklearn.preprocessing import MinMaxScaler
    z = df[df['ID'] == idd]
    z1 = df[df['ID'] == idd]
    z['Paid Loans Sum'] = temp_sum
    scaler = MinMaxScaler()
    scaler.fit_transform(df['Paid Loan Sum'].reshape(-1,1))
    
    ans = (float(scaler.transform(temp_sum)))
    
    z['Paid Loans Sum'] = ans * 5
    
    z['final'] = z['col12'] + z['Paid Loans Sum'] + z['Reference_factor'] + z['penalty_active_loans']
    z1['final'] = z['col12'] + z['Paid Loans Sum'] + z['penalty_active_loans']
    df2 = pd.DataFrame(data={'ID': idd, 'final': z['final']})
    df3 = pd.DataFrame(data={'ID': idd, 'final': z1['final']})
    
    
    ans1 = par(idd, df2)
    ans2 = par(idd, df3)
    
    lll.append(ans1[0])
    mmm.append(ans2)
    return ans1

def trend(idd):
    global lll, mmm
    lll = []
    mmm = []
    y = df[df['ID'] == idd]
    
    lis = []
    for paid_loan in (y['Paid Loans'].values):
        z = y
        lis = (z['Paid Loans'].values[0])
        li = lis[1:-1].split(', ')
        
        liss = [ int(x) for x in li ]
        
    
        temp = []
    cal = [0]*len(liss)
    for i in range(len(liss)):
        temp.append(liss[i])
        

        cal[i] = calculator(idd, sum(temp))
    

            
'''trend(1007)
print(lll)
print(mmm[0][0])'''


# In[299]:

idd = 1095
def start(idd):
    trend(idd)
    #print('List : ' , lll)
    return lll,mmm[0][0]
#start(idd)


# In[ ]:




# In[ ]:



