#!/usr/bin/env python
# coding: utf-8

# # Python API GET & Analysis

# In[12]:


# import packages
import requests
import json
from datetime import datetime


# In[2]:


response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())


# In[7]:


# json.dumps() - take in a Python object, and converts(dumps) it to a string
# json.loads() - take a JSON string, and converst(loads) it to a Python object

# a function to print Python object to a string with indent
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# In[8]:


jprint(response.json())


# In[10]:


## API with Parameters
parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
jprint(response.json())


# In[11]:


# extract pass_time
pass_time = response.json()['response']
jprint(pass_time)



# In[14]:


risetimes = []
for d in pass_time:
    time = d['risetime']
    risetimes.append(time)
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)


# In[ ]:
