#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


os.getcwd()


# In[5]:


files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])
    
all_months_data.to_csv('all_data2.csv', index=False)


# In[6]:


all_data = pd.read_csv("all_data.csv")
all_data


# # Additional Columns

# In[7]:


#Clean Data from NaN

nan_df = all_data[all_data.isnull().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data


# In[8]:


all_data['Month'] = all_data['Order Date'].str[0:2]
random = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data = random
all_data['Month'] = all_data['Month'].astype('int32')
all_data


# In[9]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# In[10]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']


# In[11]:


results = all_data.groupby('Month').sum()
# Month 12 had the most sales (December)


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


months = range(1,13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Months')


# In[14]:


# What city had the highest number of sales


# In[15]:


city = all_data['Purchase Address'].str.split(',')[0:]


# In[58]:


def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]


# In[64]:


#all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1])
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)}  ({get_state(x)})")
all_data
cities = all_data.groupby('City').sum()
cities


# In[65]:


plt.figure(figsize=(20,10))
plt.bar(cities.index, cities['Sales'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




