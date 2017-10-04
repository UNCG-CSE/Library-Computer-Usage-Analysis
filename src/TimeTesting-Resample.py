
# coding: utf-8

# # Time Testing using Resample
# #### This is a test of a semester's worth of data via resample.

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

semesterData = pd.read_csv(r'../data/SPR2017.csv')


# In[4]:

semesterData.datestamp = semesterData.datestamp.apply(pd.to_datetime)


# In[6]:

fullMatrix = semesterData.pivot(index='datestamp',columns='machineName',values='state').sort_index()


# In[7]:

def inUseConvert(state):
    offStates = ['available','restarted','offline']
    if state == 'in-use':
        return 1
    elif state in offStates:
        return 0
    else:
        return np.nan


# In[8]:

fullMatrixInts = fullMatrix.applymap(inUseConvert)


# In[9]:

fullMatrixHours = fullMatrixInts.ffill().resample('min').ffill().resample('H').sum()


# In[12]:

fullMatrixHours.info()

