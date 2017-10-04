
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

useData = pd.read_csv(r'../data/170830_StateData.csv')


# In[ ]:

useData.head()


# This is an interesting exercise demonstrating that there are occurrences that evaluated to having occurred at the exact same millisecond.

# In[ ]:

useData[pd.to_datetime(useData.dateStamp).duplicated(keep=False)]


# Verifying the status of the columns. 'dataStamp' should be a datetime64 field.

# In[ ]:

useData.dateStamp = useData.dateStamp.apply(pd.to_datetime)


# In[ ]:

useData.info()


# Testing functionality with a single computer. Working with iterating across the DataFrame later.

# In[ ]:

computerDataName = 'CITI002'


# In[ ]:

computerTimeArray = useData[useData.computerName == computerDataName]


# In[ ]:

computerTimeArray


# This turns the 'in-use' value into true, and all of the others into false. Since this analysis is based upon when a machine is not being used (as opposed to when it is offline/available/restarted) all other states are irrelevant.
# 
# Will need to investigate copy/view on this error. May need to do this as a dataframe with `.concat()`.

# In[ ]:

computerTimeArray.loc[:,'state'] = pd.Series(computerTimeArray.state == 'in-use')


# Location data is irrelevant for a machine at this point. Also, location can be derived from machine name, machine location is (at this point) not that precise.
# 
# The duplicates with regard to the indexing is no longer an issue. Since the dateStamp field before only had 'minute' precision, this has been fixed by importing data with 'millisecond' precision.

# In[ ]:

computerTimeArray


# In[ ]:

computerTimeArray = computerTimeArray.set_index('dateStamp').sort_index()


# In[ ]:

computerTimeArray


# This takes the above data and resamples it into minute increments. Value for the specific minute is put into place, while 'NaN' values will take on the previous non-NaN data.

# In[ ]:

computerTimeArrayMin = computerTimeArray.resample('T').ffill()


# In[ ]:

computerTimeArrayPerHour = computerTimeArrayMin.resample('H').sum()


# In[ ]:

computerTimeArrayPerHour


# This is a matrix of the datestamp times as the index, computers as the columns, and the state change at the intersection.

# In[ ]:

fullMatrix = useData.pivot(index='dateStamp',columns='computerName',values='state').sort_index()


# In[ ]:

fullMatrix


# While this gets the dataframe into the preferred format, it causes problems with resampling later. Testing with sample data now.

# In[ ]:

dateTestRange = pd.date_range(start='01-01-2017',end='01-02-2017',freq='s')


# In[ ]:

dateTestSeries = pd.Series(dateTestRange)


# In[ ]:

dateTestDataFrame = pd.concat([dateTestSeries,pd.Series()],axis=1)


# In[ ]:

dateTestDataFrame.info()


# In[ ]:

dateTestDataFrame.columns = ['DateTime','StateAtTime']


# In[ ]:

dateTestDataFrame.iloc[14,1] = True


# In[ ]:

dateTestDataFrame.set_index('DateTime',inplace=True)


# In[ ]:

dateTestDataFrame.head(15)


# This function converts the three off-states into a zero (0), and the single on state ('in-use') into a one (1). The remainder are left as np.nan. 
# 
# **Note: cells formatted as integer do not support np.nan, so the cells are converted to floats to accommodate it.**

# In[ ]:

def inUseConvert(state):
    offStates = ['available','restarted','offline']
    if state == 'in-use':
        return 1
    elif state in offStates:
        return 0
    else:
        return np.nan


# using the `.applymap()` to apply the inUseConvert function to each individual cell, and testing it.

# In[ ]:

print fullMatrix.applymap(inUseConvert)[fullMatrix.CITI002.notnull()].iloc[:,3]
print fullMatrix[fullMatrix.CITI002.notnull()].iloc[:,3]
print fullMatrix.applymap(inUseConvert)[fullMatrix.CITI002.notnull()].iloc[:,3] == 1
print fullMatrix.applymap(inUseConvert)[fullMatrix.CITI002.notnull()].iloc[:,3] == 0


# In[ ]:

fullMatrixInts = fullMatrix.applymap(inUseConvert)


# Testing a couple of samples here, it appears that these are the correct sums for the number of minutes per hour.

# In[ ]:

fullMatrixHours = fullMatrixInts.ffill().resample('min').ffill().resample('H').sum()
fullMatrixHours


# By changing the value in the variable testComputer, the information in the raw imported data can be compared to its column in the matrix as a whole.

# In[ ]:

testComputer = 'INC004' ## INC004 is the most dramatic thus far.
print "---------- Raw imported data ----------"
print fullMatrix[fullMatrix.loc[:,testComputer].notnull()].loc[:,testComputer]
print "\n------- Formatted Data min/hour -------"
print fullMatrixHours.loc[:,testComputer]

