
# coding: utf-8

# Weather Data

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


# gsoDataAll = pd.read_csv(r'../data/1052640.csv',low_memory=False)


# In[7]:


# gsoDataAll.columns.values


# This is just a smaller subset of the columns. Daily and Monthly rollups were ignored. Fahrenheit temps used instead of Celcius.

# In[8]:


gsoData = pd.read_csv(r'../data/1052640.csv',usecols = ['DATE', 
                                                'REPORTTPYE', 'HOURLYSKYCONDITIONS', 'HOURLYVISIBILITY', 
                                                'HOURLYPRSENTWEATHERTYPE', 'HOURLYDRYBULBTEMPF', 'HOURLYWETBULBTEMPF',
                                                'HOURLYDewPointTempF', 'HOURLYRelativeHumidity', 'HOURLYWindSpeed',
                                                'HOURLYWindDirection', 'HOURLYWindGustSpeed', 'HOURLYStationPressure',
                                                'HOURLYPressureTendency', 'HOURLYPressureChange', 'HOURLYSeaLevelPressure',
                                                'HOURLYPrecip', 'HOURLYAltimeterSetting'],
                                                low_memory = False)


# Verifying the columns.

# In[9]:


gsoData.info()


# The spelling here is frustrating.

# In[10]:


gsoData.rename(columns = {'REPORTTPYE':'REPORTTYPE'}, inplace=True)


# These seem to be start of day values:

# In[11]:


gsoData[gsoData.REPORTTYPE == 'SOD']


# Dropping **S**tart **O**f **D**ay

# In[12]:


gsoDataHourly = gsoData[gsoData.REPORTTYPE != 'SOD']


# In[13]:


gsoDataHourly.REPORTTYPE.unique()


# In[14]:


gsoDataHourly.set_index(gsoDataHourly['DATE'].apply(pd.to_datetime),inplace=True)


# In[15]:


gsoDataHourly = gsoDataHourly.drop('DATE',axis=1)


# In[16]:


gsoDataHourly.info()


# ehhh... just for the heck of it...

# In[17]:


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[18]:


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

