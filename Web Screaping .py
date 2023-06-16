#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install requests


# In[10]:


get_ipython().system('pip install Beautifulsoup')


# In[11]:


from bs4 import BeautifulSoup


# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


# In[13]:


url="https://www.bea.gov/"


# In[14]:


r=requests.get(url)


# In[62]:


soup = BeautifulSoup(r.text,'html.parser')


# In[19]:


results = soup.find_all('div',class_="blog-list-page view view-article-list view-id-article_list view-display-id-block_2 js-view-dom-id-7169b8e1eb3f5ac97424eea641c43901ce03c47145b9ca975fc7b856c800f110")


# In[25]:


headers=soup.find_all("h3")


# In[27]:


title = []


# In[32]:


title = []  # Create an empty list to store the extracted titles

for i in headers:
    title_text = i.text  # Extract the text content of each element
    title.append(title_text)  # Append the title to the 'title' list

print(title)  # Print the extracted titles


# In[33]:


result = ''.join(title)  # Convert the list back to a string
print(title)


# In[64]:


Date = soup.find_all("div", class_="date-published")


# In[65]:


Date


# In[66]:


Date_list = []

for i in Date:
    Date_text = i.text
    Date_list.append(Date_text)

print(Date_list)


# In[67]:


Paragraph = soup.find_all("p")


# In[88]:


paragraph_text = paragraph.get_text()


# In[89]:


paragraph_text


# In[95]:


integer_list = []
for pg in Paragraph:
    paragraph_text = paragraph.get_text()
    integers = re.findall(r'\d+', paragraph_text)
    integer_list.extend([int(i) for i in integers])


# In[116]:


integers = re.findall(r'\d+', paragraph_text)


# In[122]:


print(integers)


# In[140]:


data = {'Title': title,
        'Date': Date_list,
        'Value': integers}


# In[126]:


data


# In[143]:


df = pd.DataFrame(data)

print(df)


# In[144]:


df.to_csv("Web_Scrap_taiyo_ai.csv")


# In[ ]:





# In[145]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from datetime import datetime
import statsmodels.api as sm

 # Supressing warnings

import warnings             
warnings.filterwarnings('ignore')


# In[147]:


#Import Dataset

#Load the data
df = pd.read_csv(r"Web_Scrap_taiyo_ai.csv",
                 parse_dates = ['Date'],
                )


# In[148]:


df


# In[150]:


df['Date'] = pd.to_datetime(df['Date'])
df


# In[151]:


#Basic Information
df.info()
df.shape


# In[152]:


# Describe the data - Descriptive statistics.
df.describe()
df.median()


# In[153]:


df.mode()


# In[155]:



# Null values

df.isnull().sum()
# Duplicate Values

df.duplicated().sum()


# In[157]:


#It shows there is no Null and Duplicated values in the dataset
# Know the datatypes
df.dtypes
# Unique Values in the data
df['Date'].unique()


# In[158]:


# Correlation 
df.corr()


# # Visualization of Data

# ### Line Plot

# In[161]:


# line plot
plt.figure(figsize=(20, 6))
sns.lineplot(y='Value', x='Date', data=df);
plt.title('Values vs Time');
plt.xlabel('Date');
plt.ylabel('Value');


# ### Histogram

# In[163]:


plt.hist(df['Value'],color='black')


# In[164]:


### you can create a box plot for any numerical column using a single line of code.
box=df.boxplot(figsize=(8,8))


# ### Dist Plot

# In[166]:


sns.distplot(df['Value'])
plt.axvline(x=np.mean(df['Value']), c='red', ls='--', label='mean')
plt.axvline(x=np.percentile(df['Value'],25),c='green', ls='--', label = '25th percentile:Q1')
plt.axvline(x=np.percentile(df['Value'],75),c='orange', ls='--',label = '75th percentile:Q3' )
plt.legend()


# ### Scatter Plot

# In[174]:


plt.figure(figsize=(30,8))
df.plot(kind='scatter',x='Date',y='Value')
plt.show()


# In[ ]:




