
# coding: utf-8

# In[41]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LibDataImport
import weather
import cPickle
import os.path


# In[42]:

# Load utilization summary data into a DataFrame, one column per computer.
pkl = open(os.path.join('..', 'data', 'LibData.pkl'), 'rb')
utilization = cPickle.load(pkl)
pkl.close()

# Remove RRK001 because it seems to always be on, which is unlikely to be due to student use.
# Convert utilization units to %.
utilization = utilization.drop(['RRK001'], axis=1).apply(lambda x: x * 100.0)


# In[43]:

utilization.info()


# In[44]:

# Pull in weather data.
pkl = open(os.path.join('..', 'data', 'WeatherData.pkl'), 'rb')
gsoWeather = cPickle.load(pkl)
pkl.close()
gsoWeather.index


# In[45]:

# Our library data contains records from 2010-03-24 to 2017-10-19.
# The weather data contains records from 2010-07-01 to 2017-08-21.
# Trim the datasets down to the intersection of these date ranges.
gsoWeather = gsoWeather[(gsoWeather.index >= '2010-07-01') & (gsoWeather.index < '2017-08-22')]
print(gsoWeather.index)
utilization = utilization[(utilization.index >= '2010-07-01') & (utilization.index < '2017-08-22')]
print(utilization.index)


# In[46]:

# Make this notebook useful for something.
get_ipython().magic('matplotlib inline')


# In[47]:

# Resample the utilization data to daily and monthly periods for cases where we don't care about intra-day trends.
daily = utilization.resample('D').mean()
monthly = utilization.resample('M').mean()
hourlyAggregate = utilization.apply(lambda x: x.mean(), axis=1)
dailyAggregate = daily.apply(lambda x: x.mean(), axis=1)
monthlyAggregate = monthly.apply(lambda x: x.mean(), axis=1)

# There seems to be a pretty clear weekly trend here, though...
dailyAggregate.plot()


# In[48]:

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
gsoWeatherInterp = gsoWeatherCore.resample('H').interpolate()
gsoWeatherCore.head()


# In[49]:

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
matrixHourly = pd.DataFrame(hourlyAggregate, columns=['Utilization(%)']).join(gsoWeatherInterp, how='inner')
matrixDaily = pd.DataFrame(dailyAggregate, columns=['Utilization(%)']).join(dailyWeather, how='inner')
matrixMonthly = pd.DataFrame(monthlyAggregate, columns=['Utilization(%)']).join(monthlyWeather, how='inner')


# In[50]:

# It might be interesting to look at this data by each day of the week, too.
daysOfWeek = [ 'Monday'
             , 'Tuesday'
             , 'Wednesday'
             , 'Thursday'
             , 'Friday'
             , 'Saturday'
             , 'Sunday' ]

matrixDaily['Day of week'] = [daysOfWeek[d] for d in matrixDaily.index.dayofweek]


# In[51]:

# Summary by day of week...
matrixDaily.groupby(by='Day of week').mean()


# In[52]:

# When considering the entire dataset, there is no correlation between utilization and outside temperature.
matrixHourly[['Utilization(%)','HOURLYDRYBULBTEMPF']].corr()


# In[53]:

def hexPlot(x, y, title, xlabel, ylabel):
    fig = plt.figure(figsize=(16,16))
    hb = plt.hexbin(x, y, bins='log', gridsize=75)
    hb.axes.set_title(title)
    hb.axes.set_xlabel(xlabel)
    hb.axes.set_ylabel(ylabel)
    cb = fig.colorbar(hb)
    cb.set_label('log(N)')


# In[54]:

x = matrixHourly['HOURLYDRYBULBTEMPF']
y = matrixHourly['Utilization(%)']
#hexPlot(x, y, 'Aggregate computer use vs. temperature, hourly', 'Temperature(F)', 'Use(%)')


# In[55]:

merged = gsoWeatherInterp[['HOURLYDRYBULBTEMPF']].join(utilization, how='inner')
merged.info()

computerUsage = merged.drop(['HOURLYDRYBULBTEMPF'], axis=1)
temps = merged['HOURLYDRYBULBTEMPF']

temps = np.hstack([temps] * len(computerUsage.columns))
usage = np.hstack([x.values for (_,x) in computerUsage.iteritems()])
#hexPlot(temps, usage, 'Individual computer use vs. temperature, hourly', 'Temperature(F)', 'Use(%)')


# In[56]:

import seaborn as sns

matrixHourly.corr()


# In[57]:

sns.heatmap(matrixHourly.corr())


# In[58]:

utilization = utilization[1:]
gsoWeatherInterp = gsoWeatherInterp[1:]
print(utilization.head())
print(gsoWeatherInterp.head())


# In[71]:

stacked = utilization.join(gsoWeatherInterp, how='inner')
stacked = (stacked - stacked.mean()) / stacked.std()
cc = stacked.corr()


# In[74]:

fig, ax = plt.subplots(figsize=(75,75))
sns.heatmap(cc, ax=ax)

