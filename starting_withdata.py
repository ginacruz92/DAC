import pandas as pd


# In[2]:


digits = pd.read_csv("my_data_set.csv")


# In[3]:


digits.head()


# In[4]:


# Take a sample of 5
digits.sample(5)


# In[5]:


digits.describe()


# In[6]:


digits.info
