
# coding: utf-8

# # Time Testing using Resample
# #### This is a test of a semester's worth of data via resample.

# In[ ]:

import pandas as pd
import numpy as np


# In[ ]:

semesterData = pd.read_csv(r'../data/SPR2017.csv')


# In[ ]:

semesterData.datestamp = semesterData.datestamp.apply(pd.to_datetime)
semesterData.info()


# In[ ]:

from timeit import default_timer as timer

start = timer()
fullMatrix = semesterData.pivot(index='datestamp',columns='machineName',values='state').sort_index()


# In[ ]:

def inUseConvert(state):
    offStates = ['available','restarted','offline']
    if state == 'in-use':
        return 1
    elif state in offStates:
        return 0
    else:
        return np.nan


# In[ ]:

fullMatrixInts = fullMatrix.applymap(inUseConvert)


# In[ ]:

fullMatrixHours = fullMatrixInts.ffill().resample('min').ffill().resample('H').sum()
end = timer()
print(end - start) 


# In[ ]:

fullMatrixHours.info()


# In[ ]:

semesterData.head()


# In[ ]:

fullMatrixHours


# In[ ]:

import LibDataImport

start = timer()
# assume that @semesterData is sorted by datestamp.
utilization = LibDataImport.machineStatesToPercentUtilization(semesterData)
end = timer()
print(end - start)


# In[ ]:

utilization


# `fullMatrixHours` has more rows than `utilization`.  This is due to the fact that
# the earliest timestamp in `semesterData` is at `2017-01-01 06:30:28.323`.  However, no
# logon events appear in `semesterData` before `2017-01-01 20:18:20.860`.

# In[ ]:

print(fullMatrixHours.shape)
print(utilization.shape)


# In[ ]:

sortedData = semesterData.sort_values(by='datestamp')
print("First event:")
print(sortedData.iloc[0])
print("\n")
print("First in-use event:")
print(sortedData[sortedData['state']=='in-use'].iloc[0])


# Since these first few rows aren't useful to us, we'll just discard them to make direct
# comparisons easier.  We also replace `NaN`s with zeros, since the lack of usage data
# in this context can be effectively interpreted as no usage.

# In[ ]:

fullMatrixHoursZeroed = fullMatrixHours.fillna(0).iloc[14:]


# Compute the difference between the two matrices.  Drop all columns and rows where the difference
# between all values is less than two minutes.

# In[ ]:

diff = fullMatrixHoursZeroed - (utilization * 60)
diff[diff.abs() > 2].dropna(how='all').dropna(axis=1, how='all')


# ## A few highlighted discrepancies

# ### Example 1: last machine event is a login event

# In[ ]:

fullMatrixHoursZeroed['DDL002'].tail(20)


# In[ ]:

utilization['DDL002'].tail(20)


# There are only 83 records for this machine, and the last one is 'in-use'.
# This results in `fullMatrixHours` showing `DDL002` as continuously in-use after
# `2017-02-22 09:36:13.040`.

# In[ ]:

temp = sortedData[sortedData['machineName']=='DDL002']
print(temp.shape)
print(temp.tail())


# ### Example 2: incorrect usage calculation

# In[ ]:

fullMatrixHoursZeroed['DDL0001'].loc['2017-02-22 12:00:00']


# In[ ]:

utilization['DDL0001'].loc['2017-02-22 12:00:00'] * 60


# Looking specifically at events between `12:00:00` and `13:00:00` on `2017-02-22`:

# In[ ]:

temp = sortedData[(sortedData['machineName']=='DDL0001') & (sortedData['datestamp']>='2017-02-22 12:00:00') & (sortedData['datestamp']<'2017-02-22 13:00:00')]
print(temp)


# Manually summing the intervals between `in-use` and other states:

# In[ ]:

temp2 = temp['datestamp']
temp3 = [ (268809, 268810)
        , (268813, 268814)
        , (268815, 268816)
        , (268819, 268820)
        , (268823, 268824) ]

import functools
total = functools.reduce(lambda x, y: x+y, [temp2.loc[end]-temp2.loc[start] for (start,end) in temp3])
print(total)

# Now as decimal number of minutes:
print((total / pd.Timedelta(1, unit='h')) * 60)

