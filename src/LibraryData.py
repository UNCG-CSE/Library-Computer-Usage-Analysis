
# coding: utf-8

# # Converting Timestamps to Minutes Per Hour

# The following attempts to take non-uniform timestamps and do the following:
# * resample those timestamps into minutes
# * forward-fill the states
# * resample the minutes into hours, summing the minutes
# 
# The function `.resample()` changed in pandas 0.18.1, so this was a learning process.

# In[ ]:


import numpy as np
import pandas as pd
print "This should be '0.20.1':"
print "pandas:         " + str(pd.__version__)
print "This should be '1.12.1':"
print "numpy:          " + str(np.__version__)


# importing the data from the Library data sample.

# In[ ]:


useData = pd.read_csv(r'../data/170830_StateData.csv',parse_dates=[3])


# Verifying the status of the columns. 'datastamp' should be a datetime64 field.

# In[ ]:


useData.info()


# Testing functionality with a single computer. Working with iterating across the numpy array later.

# In[ ]:


computerDataName = 'CRR005'


# In[ ]:


computerTimeArray = useData[useData.machineName == computerDataName]


# In[ ]:


computerTimeArray


# This turns the 'in-use' value into true, and all of the others into false. Since this analysis is based upon when a machine is not being used (as opposed to when it is offline/available/restarted) all other states are irrelevant.
# 
# Will need to investigate copy/view on this error. May need to do this as a dataframe with `.concat()`.

# In[ ]:


computerTimeArray.loc[:,'state'] = pd.Series(computerTimeArray.state == 'in-use')


# Location data is irrelevant for a machine at this point. Also, location can be derived from machine name, machine location is (at this point) not that precise.
# 
# Pandas was giving a duplicate error due to the three non- 'in-use' states occurring simultaneously. Dropping unused columns for data duplication (machinename and location), and dropping timestamp duplications.

# In[ ]:


computerTimeArray = computerTimeArray.loc[:,'state':'datestamp'].drop_duplicates()


# In[ ]:


computerTimeArray = computerTimeArray.set_index('datestamp').sort_index()


# In[ ]:


computerTimeArray


# This takes the above data and resamples it into minute increments. Value for the specific minute is put into place, while 'NaN' values will take on the previous non-NaN data.

# In[ ]:


computerTimeArrayMin = computerTimeArray.resample('T').ffill()


# In[ ]:


computerTimeArrayPerHour = computerTimeArrayMin.resample('H').sum()


# In[ ]:


computerTimeArrayPerHour


# In[ ]:


computerNames = useData.iloc[:,0].unique()


# In[ ]:


for i in computerNames.tolist():
    print i

