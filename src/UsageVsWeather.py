
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LibDataImport
import weather


# In[ ]:

# Load utilization summary data into a DataFrame, one column per computer.
machineStates = pd.read_csv(r'../data/SPR2017.csv')
machineStates['datestamp'] = machineStates['datestamp'].apply(pd.to_datetime)
utilization = LibDataImport.machineStatesToPercentUtilization(machineStates)


# In[ ]:

utilization.info()


# In[ ]:

# Make this notebook useful for something.
get_ipython().magic('matplotlib inline')


# In[ ]:

# Resample the utilization data to daily and monthly periods for cases where we don't care about intra-day trends.
daily = utilization.resample('D').mean()
monthly = utilization.resample('M').mean()
hourlyAggregate = utilization.apply('mean', axis=1)
dailyAggregate = daily.apply('mean', axis=1)
monthlyAggregate = monthly.apply('mean', axis=1)

# There seems to be a pretty clear weekly trend here, though...
dailyAggregate.plot()


# In[ ]:

# Pull in weather data.
gsoWeather = weather.parseWeatherData('../data/1052640.csv')
gsoWeather.index


# In[ ]:

# Our library data only contains records from 2017-01-01 thru 2017-05-31.
# Trim the weather data down to the same date range.
gsoWeather = gsoWeather[gsoWeather.index <= '2017-05-31']
gsoWeather.index


# In[ ]:

# Now, we really only need some of these columns.
gsoHourlyWeather = weather.hourlyWeatherOnly(gsoWeather)

# Initially, let's just focus on temperature, wind-speed, and precipitation.
columnsOfInterest = [ 'HOURLYWETBULBTEMPF'
                    , 'HOURLYDRYBULBTEMPF'
                    , 'HOURLYWindSpeed'
                    , 'HOURLYWindGustSpeed'
                    , 'HOURLYPrecip' ]
gsoWeatherCore = gsoHourlyWeather[columnsOfInterest]

# Clean up incorrect values.
gsoWeatherCore = gsoWeatherCore.replace(to_replace='[^0-9.-]', value='', regex=True)
gsoWeatherCore = gsoWeatherCore.replace(to_replace='', value='0').apply(np.float64)


# In[ ]:

# Now if we resample this to daily or monthly aggregate values, some columns
# need to have their values averaged, and others need to be summed.

def aggregateMatrix(df, period=None):
    needAverage = df[columnsOfInterest[:-1]]
    needSum = df['HOURLYPrecip']
    if period!=None:
        needAverage = needAverage.resample(period)
        needSum = needSum.resample(period)
    periodAverage = needAverage.mean()
    periodSum = needSum.sum()
    return periodAverage.join(periodSum, how='inner')

# Now re-join these...
dailyWeather = aggregateMatrix(gsoWeatherCore, 'D')
monthlyWeather = aggregateMatrix(gsoWeatherCore, 'M')

# And finally join with library data.  This gives us individual computer usage, as well as a subset of
# the weather data, in hourly, daily, and monthly periods.
matrixHourly = pd.DataFrame(hourlyAggregate, columns=['Utilization(%)']).join(gsoWeatherCore, how='inner')
matrixDaily = pd.DataFrame(dailyAggregate, columns=['Utilization(%)']).join(dailyWeather, how='inner')
matrixMonthly = pd.DataFrame(monthlyAggregate, columns=['Utilization(%)']).join(monthlyWeather, how='inner')


# In[ ]:

# It might be interesting to look at this data by each day of the week, too.
daysOfWeek = [ 'Monday'
             , 'Tuesday'
             , 'Wednesday'
             , 'Thursday'
             , 'Friday'
             , 'Saturday'
             , 'Sunday' ]

matrixDaily['Day of week'] = [daysOfWeek[d] for d in matrixDaily.index.dayofweek]


# In[ ]:

# Summary by day of week...
matrixDaily.groupby(by='Day of week').mean()


# In[ ]:

# There is a weak positive correlation between the temperature and aggregate computer usage.
matrixHourly[['Utilization(%)','HOURLYDRYBULBTEMPF']].corr()


# In[ ]:

from pandas.plotting import scatter_matrix

# It seems that there is a pretty clear upper bound on usage that scales linearly with outside temperature.
scatter_matrix(matrixHourly[['Utilization(%)','HOURLYDRYBULBTEMPF']], alpha=0.4, figsize=(16,16), diagonal='kde')


# In[ ]:

# However it seems that temperature has little impact on the amount of use any given computer receives.

merged = gsoWeatherCore[['HOURLYDRYBULBTEMPF']].join(utilization, how='inner')
merged.info()

# Remove RRK001 because it seems to always be on, which is unlikely to be due to student use.
computerUsage = merged.drop(['HOURLYDRYBULBTEMPF', 'RRK001'], axis=1)
temps = merged['HOURLYDRYBULBTEMPF']

fig = plt.figure(figsize=(16,16))
temps = np.hstack([temps] * len(computerUsage.columns))
usage = np.hstack([x.values for (_,x) in computerUsage.iteritems()])
plt.hexbin(usage, temps, bins='log')

