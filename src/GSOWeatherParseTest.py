
# coding: utf-8

# # GSOWeatherParseTest
# 
# ## Objectives:
# ### Test the Metar package
# ### Decode the Metar codes
# #### Have csv file completely decoded for REPORTTYPE, HOURLYSKYCONDITIONS, and HOURLYPRESENTWEATHERTTYPE
# 

# In[ ]:


import numpy as np
import pandas as pd
import re
from metar import Metar


# In[ ]:


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



# In[ ]:


df=pd.read_csv(r'../data/1052640.csv')


# In[ ]:


df1 = df.loc[0]['HOURLYSKYCONDITIONS']
df1


# In[ ]:


#import re
df20 = re.sub(r'(\d)\s+(\d)', r'\1\2', df1)
df20 = re.sub('\:', '', df20)
df20


# In[ ]:


obs = Metar.Metar(df20)
print obs.string()


# In[ ]:


code = "METAR KEWR 111851Z VRB03G19KT 2SM R04R/3000VP6000FT TSRA BR FEW015 BKN040CB BKN065 OVC200 22/22 A2987 RMK AO2 PK WND 29028/1817 WSHFT 1812 TSB05RAB22 SLP114 FRQ LTGICCCCG TS OHD AND NW-N-E MOV NE P0013 T02270215"
obs = Metar.Metar(code)

# The present_weather() method summarizes the weather description (rain, etc.)
print("weather: %s" % obs.present_weather())
# The sky_conditions() method summarizes the cloud-cover observations.
print("sky: %s" % obs.sky_conditions("\n     "))

