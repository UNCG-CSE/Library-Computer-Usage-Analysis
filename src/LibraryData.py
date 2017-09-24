
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
print("This should be '0.20.1':")
print("pandas:         " + str(pd.__version__))
print("This should be '1.12.1':")
print("numpy:          " + str(np.__version__))


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


for i in computerNames.tolist():
    print(i)


# ## Alternative method of computing per-machine utilization

# In[ ]:


# Compute the intervals during which each computer was in use.
# @df must be a pandas DataFrame with columns ['machineName',
# 'location', 'state', 'datestamp'].
# Returns a dictionary keyed by 'machineName' with values
# of (timestamp, timerange) corresponding to sessions of machine
# usage.
def toUsageIntervals(df):
    # Bin records by @machineName.
    binned = {}
    names = df['machineName'].unique()
    for name in names:
        matching = df[df['machineName'] == name]
        binned[name] = matching.loc[:,'state':'datestamp'].sort_values(by='datestamp')

    # Compute date ranges of usage for each machine.
    for (name, frame) in binned.items():
        # Mark which records correspond to 'in-use'.
        inUse = list(frame['state'] == 'in-use')
        # Each consecutive True/False corresponds to a period of activity.
        # Compute a DateRange from each consecutive True/False pair.
        indexedInUse = list(zip(range(0,len(inUse),1), inUse))
        transitions = [(frame.iloc[x[0]].loc['datestamp'], frame.iloc[y[0]].loc['datestamp']) for (x, y) in zip(indexedInUse[:-1], indexedInUse[1:]) if x[1]==True and y[1]==False]
        dateRanges = [(x, y-x) for (x, y) in transitions]
        binned[name] = dateRanges
    return binned

from pandas.tseries.offsets import *
import functools
import itertools

# Convert date ranges into hourly usage data.
def usageIntervalsToPercentUtilization(binned, period='h'):
    def dateRangeToPeriodUtilization(begin, length):
        # Round the starting time down to the nearest period.
        start = begin.floor(period)
        if ((begin + length).floor(period) == start):
            # If we don't cross a period boundary, just return the amount of time
            # spent 'in-use' for this period.
            return [(start, pd.Timedelta(length))]
        else:
            # Otherwise, we need to break the session down by period, according to wall-time.
            # We already have the beginning of this interval.  Round up the end time to the
            # nearest period to get the end-point of the interval.
            end = (begin + length).ceil(period)
            # Now create a list of timestamps corresponding to periods on the clock for this
            # session.
            # One would think 'closed=None' means don't include the first or last value
            # in the interval.  This doesn't seem to be the case though, so manually remove
            # those values.  Otherwise, we end up with two copies of the start period, and
            # two copies of the end period.
            periods = pd.date_range(start, end, freq=period, closed=None)[1:-1]
            # Compute the amount of time spent 'in-use' in the first hour-long interval.
            first = pd.Timedelta('1' + period) - (begin - start)
            # Similarly for the last hour-long interval.
            last = pd.Timedelta('1' + period) - (end - (begin + length))
            # Create a list of (timestamp,timerange) pairs giving the total amount of time
            # spent 'in-use' for each period-long interval.
            return list(zip([start] + list(periods), [first] + ([pd.Timedelta('1' + period)] * (len(periods) - 1)) + [last]))

    def concat(lists):
        return functools.reduce(lambda x, y: x + y, lists)

    def nameAndDateRangeToDataFrame(name, dateRanges):
        if len(dateRanges) == 0:
            # Use [] as a null value.
            return []
        # Convert each date range into a list of (timestamp,timerange) where each timestamp
        # corresponds to a period within the timerange.
        next_ = concat(map(lambda x: dateRangeToPeriodUtilization(x[0], x[1]), dateRanges))
        # Group and sum times by period to remove duplicate periods, which would happen if
        # we have multiple timeranges within a period, e.g. if we have two entries
        # ('2017-08-31 09:02:00', '+00:05:00') and ('2017-08-31 09:10:00', '+00:13:00').
        dic = {}
        for (x, y) in next_:
            if x not in dic:
                dic[x] = y
            else:
                dic[x] += y
        # Group the results into a pair of ([timestamp],[timerange]) with unique timestamps.
        z = list(zip(*dic.items()))
        utilization = [x / pd.Timedelta(1, unit=period) for x in z[1]]
        df = pd.DataFrame({'Date': pd.Series(z[0]), name: pd.Series(utilization)}).set_index('Date')
        return [df]

    dfs = concat(map(lambda x: nameAndDateRangeToDataFrame(x[0], x[1]), binned.items()))
    return functools.reduce(lambda x, y: x.join(y, how='outer'), dfs)
    #return list(map(lambda x: x[1], binned.items()))

utilization = usageIntervalsToPercentUtilization(toUsageIntervals(useData))
utilization.fillna(value=0, inplace=True)


# In[ ]:


crr005 = utilization['CRR005']
crr005.where(lambda x: x>0).dropna()


# In[ ]:


computerTimeArrayPerHour.where(lambda x: x>0).dropna()

