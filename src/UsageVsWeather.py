
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LibDataImport
import weather
import cPickle
import os.path


# In[2]:

# Load utilization summary data into a DataFrame, one column per computer.
pkl = open(os.path.join('..', 'data', 'LibData.pkl'), 'rb')
utilization = cPickle.load(pkl)
pkl.close()

# Remove RRK001 because it seems to always be on, which is unlikely to be due to student use.
# Convert utilization units to %.
utilization = utilization.drop(['RRK001'], axis=1).apply(lambda x: x * 100.0)


# In[3]:

utilization.info()


# In[4]:

# Pull in weather data.
pkl = open(os.path.join('..', 'data', 'WeatherData.pkl'), 'rb')
gsoWeather = cPickle.load(pkl)
pkl.close()
gsoWeather.index


# In[5]:

# Our library data contains records from 2010-03-24 to 2017-10-19.
# The weather data contains records from 2010-07-01 to 2017-08-21.
# Trim the datasets down to the intersection of these date ranges.
gsoWeather = gsoWeather[(gsoWeather.index >= '2010-07-01') & (gsoWeather.index < '2017-08-22')]
print(gsoWeather.index)
utilization = utilization[(utilization.index >= '2010-07-01') & (utilization.index < '2017-08-22')]
print(utilization.index)


# In[6]:

# Make this notebook useful for something.
get_ipython().magic('matplotlib inline')


# In[7]:

# Resample the utilization data to daily and monthly periods for cases where we don't care about intra-day trends.
daily = utilization.resample('D').mean()
monthly = utilization.resample('M').mean()
hourlyAggregate = utilization.apply(lambda x: x.mean(), axis=1)
dailyAggregate = daily.apply(lambda x: x.mean(), axis=1)
monthlyAggregate = monthly.apply(lambda x: x.mean(), axis=1)

# There seems to be a pretty clear weekly trend here, though...
dailyAggregate.plot()


# In[8]:

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


# In[9]:

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


# In[10]:

# It might be interesting to look at this data by each day of the week, too.
daysOfWeek = [ 'Monday'
             , 'Tuesday'
             , 'Wednesday'
             , 'Thursday'
             , 'Friday'
             , 'Saturday'
             , 'Sunday' ]

matrixDaily['Day of week'] = [daysOfWeek[d] for d in matrixDaily.index.dayofweek]


# In[11]:

# Summary by day of week...
matrixDaily.groupby(by='Day of week').mean()


# In[12]:

# When considering the entire dataset, there is no correlation between utilization and outside temperature.
matrixHourly[['Utilization(%)','HOURLYDRYBULBTEMPF']].corr()


# In[13]:

def hexPlot(x, y, title, xlabel, ylabel):
    fig = plt.figure(figsize=(16,16))
    hb = plt.hexbin(x, y, bins='log', gridsize=75)
    hb.axes.set_title(title)
    hb.axes.set_xlabel(xlabel)
    hb.axes.set_ylabel(ylabel)
    cb = fig.colorbar(hb)
    cb.set_label('log(N)')


# In[14]:

x = matrixHourly['HOURLYDRYBULBTEMPF']
y = matrixHourly['Utilization(%)']
#hexPlot(x, y, 'Aggregate computer use vs. temperature, hourly', 'Temperature(F)', 'Use(%)')


# In[15]:

merged = gsoWeatherInterp[['HOURLYDRYBULBTEMPF']].join(utilization, how='inner')
merged.info()

computerUsage = merged.drop(['HOURLYDRYBULBTEMPF'], axis=1)
temps = merged['HOURLYDRYBULBTEMPF']

temps = np.hstack([temps] * len(computerUsage.columns))
usage = np.hstack([x.values for (_,x) in computerUsage.iteritems()])
#hexPlot(temps, usage, 'Individual computer use vs. temperature, hourly', 'Temperature(F)', 'Use(%)')


# In[16]:

import seaborn as sns

matrixHourly.corr()


# In[17]:

sns.heatmap(matrixHourly.corr())


# In[18]:

utilization = utilization[1:]
gsoWeatherInterp = gsoWeatherInterp[1:]
print(utilization.head())
print(gsoWeatherInterp.head())


# In[19]:

attributes = pd.read_csv(os.path.join('..', 'data', 'computerAttributes.csv'))
attributes.index = attributes['computerName']
machinesOfInterest = [x for x in attributes.index if attributes.loc[x]['requiresLogon']==True]


# In[20]:

stacked = utilization[machinesOfInterest].join(gsoWeatherInterp, how='inner')
# Only look at records occuring while classes are in session.  This doesn't account for things like spring-break (yet).
# Grab records from 01-17 (classes begin) to 05-12 (last day of class), and from 08-15 (classes begin) to 12-05 (last day of class).
# These dates were determined from the 2016 academic calendar, and may be slightly different for other years.
filtered = stacked[((stacked.index.dayofyear >= 17) & (stacked.index.dayofyear <= 131)) | ((stacked.index.dayofyear >= 233) & (stacked.index.dayofyear <= 338))]
cc = filtered.corr()


# ## Correlation heat matrix of individual computer use and hourly weather

# In[21]:

fig, ax = plt.subplots(figsize=(75,75))
sns.heatmap(cc, ax=ax)


# In[22]:

locations = attributes.loc[machinesOfInterest][['computerName', 'location']].groupby(by='location')


# In[23]:

groups = {}
for (k, vs) in locations:
    stacked_ = utilization[vs['computerName'].values].join(gsoWeatherInterp, how='inner')
    stacked_ = (stacked_ - stacked_.mean()) / stacked_.std()
    groups[k] = stacked_
groups.keys()


# ## Groups along the main diagonal
# Computers are grouped by 'location' attribute of `computerAttributes.csv`.

# ### Reading rooms

# In[24]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['Reading Room'].corr(), ax=ax)


# ### Checkout desk

# In[25]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['Checkout Desk'].corr(), ax=ax)


# ### DMC

# In[26]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['DMC'].corr(), ax=ax)


# ### Information commons

# In[27]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['Info Commons'].corr(), ax=ax)


# ### RIS

# In[28]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['RIS'].corr(), ax=ax)


# ### Music library

# In[29]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['Music Library'].corr(), ax=ax)


# ### Tower

# In[30]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['Tower'].corr(), ax=ax)


# ### CITI lab

# In[31]:

_, ax = plt.subplots(figsize=(16,16))
sns.heatmap(groups['CITI Lab'].corr(), ax=ax)


# ## Comparing usage on rainy vs. non-rainy days

# In[32]:

rainy = filtered[filtered['HOURLYPrecip'] > 0.01]
dry = filtered[filtered['HOURLYPrecip'] <= 0.01]


# In[33]:

print(rainy.shape)
print(dry.shape)
print(filtered.shape)


# ### Average use per computer

# In[36]:

from scipy import stats
print(stats.ttest_ind(rainy.mean(axis=0), dry.mean(axis=0)))
print(stats.ttest_rel(rainy.mean(axis=0), dry.mean(axis=0)))


# ### Hourly use per computer

# In[37]:

test_results = {}
for x in machinesOfInterest:
    test_results[x] = stats.ttest_ind(rainy[x].values, dry[x].values, equal_var=False)


# In[38]:

for (computer, test_result) in sorted(test_results.iteritems(), key=lambda x: x[1].pvalue, reverse=True):
    print(computer + ":")
    print(test_result)


# ## Average rainy-day use of machines near windows vs. not

# In[39]:

rainy_with_window = rainy[[x for x in machinesOfInterest if attributes.loc[x]['adjacentWindow']==True]].mean(axis=0)
rainy_without_window = rainy[[x for x in machinesOfInterest if attributes.loc[x]['adjacentWindow']==False]].mean(axis=0)
print(rainy_with_window.shape)
print(rainy_without_window.shape)


# In[40]:

stats.ttest_ind(rainy_without_window, rainy_with_window)

