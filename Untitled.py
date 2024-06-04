#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[15]:


company = pd.read_excel('Company_wise.xlsx')


# In[16]:


company.rename(columns={'Bond\nNumber':'Bond Number'},inplace=True)


# In[17]:


company.head(5)


# In[19]:


party = pd.read_excel('Party_wise.xlsx')


# In[20]:


party.head(5)


# In[21]:


df_inner = pd.merge(company, party, on='Bond Number', how='inner')


# In[22]:


df_inner.head(5)


# In[26]:


df_new = df_inner[['Sr No._x','Bond Number','Date of\nPurchase','Name of the Purchaser','Name of the Political Party','Denominations_x','Status']]


# In[27]:


df_new.head(5)


# In[31]:


df_test = df_new[df_new['Name of the Political Party'] == 'BHARATIYA JANATA PARTY']


# In[32]:


df_test


# In[44]:


df_final = df_test.sort_values('Date of\nPurchase',ascending=False)


# In[45]:


df_final1 = df_final[df_final['Status']=='Paid']


# In[46]:


df_final1


# In[52]:


df_list = pd.Series(df_final1['Name of the Purchaser'])


# In[59]:


df_final3 = df_list.value_counts()


# In[61]:


df_final3


# In[65]:


df_final3.head(50)


# In[ ]:




