#!/usr/bin/env python
# coding: utf-8

# In[4]:


import markdown2
import os


# In[32]:


def return_directories():
    ## TODO rewrite function to use os.path.isdir
    directories = list()
    for thing in os.listdir():
        if '.' not in thing:
            directories.append(thing)
    return directories


# In[33]:


return_directories()
directories = return_directories()


# In[40]:


# iterates through directories creates an array of dicts, a dictionary for each directory.
def create_website_structure(directories):
    for directory in directories:
        print(directory)
        print(os.listdir(directory))
        print()


# In[ ]:




