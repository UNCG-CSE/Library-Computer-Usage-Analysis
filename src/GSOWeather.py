
# coding: utf-8

# # GSOWeather
# 
# ## Objectives:
# ### Plot any hourly weather condition over time
# 
#     
# 

# In[1]:

import numpy as np
import pandas as pd
import GSOWeather


# In[9]:

gsoDataAll = GSOWeather.parseWeatherData('../data/1052640.csv')


# In[6]:

def displayWeatherData(array):
    print array.columns.values


# In[10]:

#How to use the display method
displayWeatherData(gsoDataAll)


# This is just a smaller subset of the columns. Daily and Monthly rollups were ignored. Fahrenheit temps used instead of Celcius.

# In[15]:

gsoDataHourly = GSOWeather.hourlyWeatherOnly(gsoDataAll)


# Verifying the columns.

# In[16]:

gsoDataHourly.info()


# The spelling here is frustrating.

# In[17]:

gsoDataHourly.REPORTTYPE.unique()


# In[19]:

gsoDataHourly


# ehhh... just for the heck of it...

# In[20]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[21]:

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

