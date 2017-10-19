
# coding: utf-8

# # GSOWeather
# 
# ## Objectives:
# ### Plot any hourly weather condition over time
# 
#     
# 

# ## Task 1:
# ### Plot Hourly precipitation over time

# In[73]:



import numpy as np
import pandas as pd


# In[74]:


# Make a dataframe of the columns we need 
GraphingColumns = ['DATE',
'REPORTTPYE',
'HOURLYPrecip',
'HOURLYWindSpeed']
GraphingDF = pd.read_csv(r'../data/1052640.csv',usecols = GraphingColumns, low_memory = False)


# In[75]:


# Rename the Report'tpye' column to prevent headaches 
GraphingDF.rename(columns = {'REPORTTPYE':'REPORTTYPE'}, inplace=True)


# In[76]:


# Drop StartOfDay values (always NaN)
GraphingDF = GraphingDF[GraphingDF.REPORTTYPE != 'SOD']


# In[77]:


# Index based on DATE, then drop DATE
GraphingDF.set_index(GraphingDF['DATE'].apply(pd.to_datetime),inplace=True)
GraphingDF = GraphingDF.drop('DATE',axis=1)

import matplotlib.pyplot as plt
%matplotlib inline
# In[78]:



# Graph the hourly precipitation (Finally!)
dateTime = GraphingDF.index.values
HourlyPrecipitation = pd.to_numeric(GraphingDF.loc[:,'HOURLYPrecip'].values,errors='coerce')


Precip_chart = plt.figure(figsize=(16,8))
precip = plt.plot(dateTime, HourlyPrecipitation,label= 'HOURLY Precipitation (inches)')

plt.title(' HOURLY Precipitation in inches')

plt.ylabel('precip')
plt.xlabel('time')
plt.legend(loc=0);


# In[79]:


# Graph Wind Speed
#dateTime = GraphingDF.index.values
HourlyWindSpeed = GraphingDF.loc[:,'HOURLYWindSpeed']

Precip_chart = plt.figure(figsize=(16,8))
precip = plt.plot(dateTime, HourlyWindSpeed,label= 'HOURLY Wind Speed (mph)')

plt.title(' HOURLY WindSpeed in mph')

plt.ylabel('mph')
plt.xlabel('time')
plt.legend(loc=0);


# # Below this cell is work from before 1st presentation

# ### Defining variables. hourlyColumns may be altered later, but this is what we are using for now

# In[80]:



hourlyColumns = ['DATE',
'REPORTTPYE',
'HOURLYSKYCONDITIONS',
'HOURLYVISIBILITY',
'HOURLYPRSENTWEATHERTYPE',
'HOURLYWETBULBTEMPF',
'HOURLYDRYBULBTEMPF',
'HOURLYDewPointTempF',
'HOURLYRelativeHumidity',
'HOURLYWindSpeed',
'HOURLYWindDirection',
'HOURLYWindGustSpeed',
'HOURLYStationPressure',
'HOURLYPressureTendency',
'HOURLYPressureChange',
'HOURLYSeaLevelPressure',
'HOURLYPrecip',
'HOURLYAltimeterSetting']


# In[81]:



#Defining functions - all together so we can see them and know what we have to work with
# without scrolling through entire program


# In[82]:



def getAllWeatherData():
    return pd.read_csv(r'../data/1052640.csv',low_memory=False)


# In[83]:



def getHourlyWeatherData():
    return pd.read_csv(r'../data/1052640.csv',usecols = hourlyColumns, low_memory = False)


# In[84]:



def displayWeatherData(array):
    print array.columns.values


# In[85]:



#delaring variables from the functions - don't need to know exactly what is in them to use them
gsoDataAll = getAllWeatherData()
gsoDataHours = getHourlyWeatherData()


# In[86]:



#How to use the display method
displayWeatherData(gsoDataAll)
displayWeatherData(gsoDataHours)


# This is just a smaller subset of the columns. Daily and Monthly rollups were ignored. Fahrenheit temps used instead of Celcius.

# In[87]:



gsoData = getHourlyWeatherData()


# Verifying the columns.

# In[88]:



gsoData.info()


# The spelling here is frustrating.

# In[89]:



gsoData.rename(columns = {'REPORTTPYE':'REPORTTYPE'}, inplace=True)


# These seem to be start of day values:

# In[90]:



gsoData[gsoData.REPORTTYPE == 'SOD']  


# Dropping **S**tart **O**f **D**ay

# In[91]:



gsoDataHourly = gsoData[gsoData.REPORTTYPE != 'SOD']


# In[92]:



gsoDataHourly.REPORTTYPE.unique()


# In[93]:



gsoDataHourly.set_index(gsoDataHourly['DATE'].apply(pd.to_datetime),inplace=True)


# In[94]:



gsoDataHourly = gsoDataHourly.drop('DATE',axis=1)


# In[95]:



gsoDataHourly.info()


# ehhh... just for the heck of it...

# In[96]:



import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[97]:



dateTime = gsoDataHourly.index.values
tempWetBulbInF = gsoDataHourly.loc[:,'HOURLYWETBULBTEMPF'].values
tempDryBulbInF = pd.to_numeric(gsoDataHourly.loc[:,'HOURLYDRYBULBTEMPF'].values,errors='coerce')



temp_chart = plt.figure(figsize=(16,8))
temp1 = plt.plot(dateTime, tempWetBulbInF, label= 'Wet Bulb (F)')
temp2 = plt.plot(dateTime, tempDryBulbInF, label= 'Dry Bulb (F)')

plt.title('HourlyBulbTemp in degrees F')

plt.ylabel('Temp')
plt.xlabel('time')
plt.legend(loc=0);

