#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[89]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading datasets

# In[31]:


df=pd.read_csv('hotel_bookings 2.csv')


# # Explore data analysis and data cleaning

# In[32]:


df.head()


# In[33]:


df.tail()


# In[34]:


df.shape


# In[35]:


df.columns


# In[36]:


df.info()


# In[37]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[38]:


df.describe(include='object')


# In[39]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[40]:


df.isnull().sum()


# In[41]:


df.drop(['company','agent'],axis=1, inplace= True)
df.dropna(inplace=True)


# In[42]:


df.describe()


# In[45]:


df['adr'].plot(kind='box')


# In[44]:


df=df[df['adr']<5000]


# # Data analysis and visualization

# In[56]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)

import matplotlib.pyplot as plt


plt.figure(figsize=(5, 4))
plt.title('Reservation status count')
plt.bar(['Not cancelled', 'Cancelled'], df['is_canceled'].value_counts(), edgecolor='k', width=0.7)
plt.show()


# 

# In[66]:




import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues') 
legend_labels, _ = ax1.get_legend_handles_labels()
plt.title('Reservation in different hotels',size=20)
plt.xlabel('hetel')
plt.ylabel('number of reservation')
plt.show()
ax1.legend(bbox_to_anchor=(1, 1))  
plt.show()


# In[73]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[75]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[76]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[82]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20,8))
plt.title('Average Daily rate in City and Resort Hotel',fontsize=30)
plt.plot(resort_hotel.index, resort_hotel['adr'],label='resort hotel')
plt.plot(city_hotel.index, city_hotel['adr'],label='city hotel')
plt.legend(fontsize = 20)
plt.show()


# In[86]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled', data=df, palette='bright')
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('reservation status per month',size=20)
plt.xlabel('Month')
plt.ylabel('Number of reservation')
plt.legend(['not cancelled','cancelled'])
plt.show()


# In[94]:



import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 8))
plt.title('ADR per month', fontsize=30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[109]:


cancelled_data=df[df['is_canceled']==1]
top_10_country=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()


# In[100]:


df['market_segment'].value_counts()


# In[101]:


df['market_segment'].value_counts(normalize= True)


# In[111]:


cancelled_data['market_segment'].value_counts(normalize= True)


# In[131]:


cancelled_df_adr=cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace= True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data=df[df['is_canceled']==0]
not_cancelled_df_adr=not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace= True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize= (20,6))
plt.title('Average Daily rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend()
plt.show()


# In[132]:


cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016')&(cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016')&(not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[133]:


plt.figure(figsize= (20,6))
plt.title('Average Daily rate',fontsize='20')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend(fontsize='20')
plt.show()


# In[ ]:





# In[ ]:




