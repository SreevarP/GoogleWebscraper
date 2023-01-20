#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup  
from urllib3 import request
import requests
import re


# In[2]:


def genSearch(query):
    root = "https://www.google.com/search?q="
    search_query = root + query
    return search_query


# In[3]:


genSearch('grass')


# In[4]:


data = requests.get(genSearch('grass'))


# In[5]:


with open ('data.html', 'w') as f:
    f.write(data.text)
    


# In[6]:


with open('data.html','r') as f:
    raw_html_data = f.read()


# In[7]:


doc = BeautifulSoup(raw_html_data, 'html5lib')


# In[11]:


#links
for item in doc.find_all('div', attrs={'class':'egMi0 kCrYT'}):
    raw_link = (item.find('a', href=True)['href'])
    link = raw_link.split('/url?q=')[1].split('&sa=U')[0]
    print(link)


# In[12]:


#desriptions
for item in doc.find_all('div', attrs={'class':'kCrYT'}):
    
    descriptions = (str(item.text))
    print(descriptions)
    


# In[13]:


#descirptions
for item in doc.find_all('div', attrs={'class':'BNeawe s3v9rd AP7Wnd'}):
    
    descriptions = (str(item.text))
    print(descriptions)


# In[14]:


#Link Title Better
for item in doc.find_all('div', attrs={'class':'BNeawe vvjwJb AP7Wnd'}):
    title = (item.text)
    print(title)


# In[14]:


#Special Cases - Exeternal Links Title
for item in doc.find_all('a', attrs={'class': 'BVG0Nb'}):
    print(item.text)
    print("  ")


# In[15]:


#Special Cases - Exeternal Links 
for item in doc.find_all('a', attrs={'class': 'BVG0Nb'}):
    r = str(item) 
    ec = r.split()[2].split('=')[2].split('%')[0].split(';imgrefurl')[0].split('.jpg&amp')[0]
    print(ec)


# In[ ]:




