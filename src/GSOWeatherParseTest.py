
# coding: utf-8

# # GSOWeatherParseTest
# 
# ## Objectives:
# ### Test the Metar package
# ### Decode the Metar codes
# #### Have dataframe completely decoded for HOURLYSKYCONDITIONS and HOURLYPRESENTWEATHERTTYPE
# 

# In[165]:


import numpy as np
import pandas as pd
import re
from metar import Metar


# In[166]:


####THIS IS A TEST SAMPLE LOOKING AT WHAT PYTHON_METAR CAN DO####

# A sample METAR report
code = "METAR KEWR 111851Z VRB03G19KT 2SM R04R/3000VP6000FT TSRA BR FEW015 BKN040CB BKN065 OVC200 22/22 A2987 RMK AO2 PK WND 29028/1817 WSHFT 1812 TSB05RAB22 SLP114 FRQ LTGICCCCG TS OHD AND NW-N-E MOV NE P0013 T02270215"

print("-----------------------------------------------------------------------")
print("METAR: ",code)
print("-----------------------------------------------------------------------")

# Initialize a Metar object with the coded report
obs = Metar.Metar(code)

# Print the individual data

# The 'station_id' attribute is a string.
print("station: %s" % obs.station_id)

if obs.type:
  print("type: %s" % obs.report_type())

# The 'time' attribute is a datetime object
if obs.time:
  print("time: %s" % obs.time.ctime())

# The 'temp' and 'dewpt' attributes are temperature objects
if obs.temp:
  print("temperature: %s" % obs.temp.string("C"))

if obs.dewpt:
  print("dew point: %s" % obs.dewpt.string("C"))

# The wind() method returns a string describing wind observations
# which may include speed, direction, variability and gusts.
if obs.wind_speed:
  print("wind: %s" % obs.wind())

# The peak_wind() method returns a string describing the peak wind 
# speed and direction.
if obs.wind_speed_peak:
  print("wind: %s" % obs.peak_wind())

# The visibility() method summarizes the visibility observation.
if obs.vis:
  print("visibility: %s" % obs.visibility())

# The runway_visual_range() method summarizes the runway visibility
# observations.
if obs.runway:
  print("visual range: %s" % obs.runway_visual_range())

# The 'press' attribute is a pressure object.
if obs.press:
  print("pressure: %s" % obs.press.string("mb"))

# The 'precip_1hr' attribute is a precipitation object.
if obs.precip_1hr:
  print("precipitation: %s" % obs.precip_1hr.string("in"))

# The present_weather() method summarizes the weather description (rain, etc.)
print("weather: %s" % obs.present_weather())

# The sky_conditions() method summarizes the cloud-cover observations.
print("sky: %s" % obs.sky_conditions("\n     "))

# The remarks() method describes the remark groups that were parsed, but 
# are not available directly as Metar attributes.  The precipitation, 
# min/max temperature and peak wind remarks, for instance, are stored as
# attributes and won't be listed here.
if obs._remarks:
  print("remarks:")
  print("- "+obs.remarks("\n- "))

print("-----------------------------------------------------------------------\n")



# In[167]:


df=pd.read_csv(r'../data/1052640.csv')


# In[168]:


df.rename(columns = {'REPORTTPYE':'REPORTTYPE'}, inplace=True)


# In[169]:


df = df[df.REPORTTYPE != 'SOD']
df = df[df.REPORTTYPE != 'FM-12']
df.REPORTTYPE.unique()


# In[170]:


def skyConditionsFormat(x):
    splitting_x = re.split('(\W+)', x)
    for i in splitting_x:
        if i == ' ':
            pass
        elif len(i) < 5:
            hash2 = i[:3] + '0' + i[3:]
            splitting_x = [j.replace(i, hash2) for j in splitting_x]
        else:
            pass 
    return ''.join(splitting_x)


# In[171]:


def getSkyConditions(x):
    if x in ('CLR:00', 'CLR00:000000', 'CLR0:0000'):
        return 'Clear sky'
    elif x in ('X00 SCT70', '0'):
        pass
    elif "s" in x:
        pass
    else:
        obs = Metar.Metar(x)
        return obs.sky_conditions()


# In[172]:


def getWeatherConditions(y):
    if y in ('0'):
        pass
    elif "s" in y:
        pass
    else:
        obs = Metar.Metar(y)
        return obs.present_weather()


# ### SKYCONDITIONS translates the codes properly
# ##### Had to remove the 2 integers before the Sky code EX) FEW:01 XXX; the "01" is the layer amount used in conjunction with the sky condition code given in eighths (oktas) so 01-02 correspond to the code FEW so I removed these integers since they correspond to the code it follows and so that the metar package would also work in translating 
# ###### I had to also remove some data that had the "s" ("Suspect value" that Brown mentioned) within the data, these values continued to give errors so I had them skipped during translation
# ###### Also at the moment I have the 'NaN' values replaced with '' but I can replace if needed

# #### Remove chars : _ and 2 integers following SKYCONDITIONS code; looking at LCD shows these 2 digits correspond to the SKYCONDITIONS code it follows

# In[173]:


df['HOURLYSKYCONDITIONS'] = df['HOURLYSKYCONDITIONS'].str.replace(r'\:\d{2}\s', '')


# In[174]:


df['HOURLYSKYCONDITIONS'] = df['HOURLYSKYCONDITIONS'].replace(np.nan, '', regex=True)


# ### 3 Skyconditions values with the "s"  

# In[175]:


df[df['HOURLYSKYCONDITIONS'].str.contains("s")]


# #### Translate code

# In[176]:


df['HOURLYSKYCONDITIONS'] = df['HOURLYSKYCONDITIONS'].apply(skyConditionsFormat)
df['HOURLYSKYCONDITIONS'] = df['HOURLYSKYCONDITIONS'].apply(getSkyConditions)
df


# ### HOURLYPRESENTWEATHERTYPE translates the codes properly
# ###### I had to also remove some data that had the "s" ("Suspect value" that Brown mentioned) within the data, these values continued to give errors so I had them skipped during translation
# ###### Also at the moment I have the 'NaN' values replaced with '' but I can replace if needed

# In[177]:


df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].str.replace(r'\:\d*\s', ' ')
df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].str.replace(r'\:\d*', ' ')
df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].str.replace(r'\|', '')
df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].str.rstrip()


# In[178]:


df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].replace(np.nan, '', regex=True)


# ### 29 HourlyWeatherType values with the "s"  

# In[179]:


df[df['HOURLYPRSENTWEATHERTYPE'].str.contains("s")]


# ###### Translate codes

# In[180]:


df['HOURLYPRSENTWEATHERTYPE'] = df['HOURLYPRSENTWEATHERTYPE'].apply(getWeatherConditions)
df

