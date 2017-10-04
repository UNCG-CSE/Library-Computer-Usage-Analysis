
# coding: utf-8

# # LibraryData
# 
# ## Objectives:
# ### Convert timestamps to minutes per hour
# ### Display computer id with total minutes used per hour, total log-ons in same hour

# The following attempts to take non-uniform timestamps and do the following:
# * resample those timestamps into minutes
# * forward-fill the states
# * resample the minutes into hours, summing the minutes
# 
# The function `.resample()` changed in pandas 0.18.1, so this was a learning process.

# In[ ]:

import numpy as np
import pandas as pd
import library_data
print "This should be '0.20.1':"
print "pandas:         " + str(pd.__version__)
print "This should be '1.12.1':"
print "numpy:          " + str(np.__version__)


# importing the data from the Library data sample.

# In[ ]:

useData = library_data.parseLibraryData(r'../data/170830_StateData.csv')


# In[ ]:

useData.head()


# This is an interesting exercise demonstrating that there are occurrences that evaluated to having occurred at the exact same millisecond.

# In[ ]:

useData[pd.to_datetime(useData.dateStamp).duplicated(keep=False)]


# Verifying the status of the columns. 'dataStamp' should be a datetime64 field.

# In[ ]:

useData.info()


# Testing functionality with a single computer. Working with iterating across the DataFrame later.

# In[ ]:

fullMatrix = library_data.toHourlyUsage(useData)


# In[ ]:

fullMatrix


# By changing the value in the variable testComputer, the information in the raw imported data can be compared to its column in the matrix as a whole.

# In[ ]:

testComputer = 'INC004' ## INC004 is the most dramatic thus far.
print "---------- Raw imported data ----------"
print useData[useData['computerName']==testComputer]
print "\n------- Formatted Data min/hour -------"
print fullMatrix.loc[:,testComputer]

