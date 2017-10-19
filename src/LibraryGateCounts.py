
# coding: utf-8

# # Library Gate Counts
# #### This working with visualization and processing with the library gate counts.

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


gateCounts = pd.read_csv(r'../data/LibraryGateCounts.csv')
gateCounts['Date'] = gateCounts['Date'].apply(pd.to_datetime)


# - The gate counts are taken twice a day, once at open and once at close.
# - Jackson Library: College Avenue entrance (CLG)
# - Jackson Library: EUC Connector entrance (CON)
# 
# A gate number increases by one if a person regardless of the direction traveled. The calculation below is based upon the average of the differences between the numbers at open and at close.
# 
# 

# In[ ]:


gateCounts['Patrons'] =((gateCounts['CLG-CLOSE'] - gateCounts['CLG-OPEN']) + (gateCounts['CON-CLOSE'] - gateCounts['CON-OPEN']))/2
gateCounts.head()


# In[ ]:


gateCounts.iloc[1,0]


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# manually mapping colors to days

# In[ ]:


dayColors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'indigo',
    'violet'
    ]
#Rotating the colors to get the rainbow to appear correctly.
dayColors = dayColors[5:]+ dayColors[:5]


# In[ ]:


import calendar


# Some interesting correlations to the visuals below:
# - 01/17/17: Classes begin
# - 03/11/17: Spring Break begins
# - 03/20/17: Spring Break ends
# - 05/03/17: Reading day
# - 05/04/17: Finals start
# - 05/12/17: Commencement

# In[ ]:


plt.figure(figsize=(16,8))
plt.grid(b=True)
plt.xticks(gateCounts.index.values[::7], gateCounts.Date.dt.strftime("%Y-%m-%d")[::7], rotation=90)
for i in range(7):
    plt.plot(gateCounts.index.values[i::7],gateCounts['Patrons'][i::7].values,                c=dayColors[i],                label=calendar.day_name[gateCounts.iloc[i,0].weekday()]);
plt.legend();


# Correlating gate count to weather.

# In[ ]:


weatherData = pd.read_csv(r'../data/1052640.csv',low_memory=False,usecols =['DATE','HOURLYWETBULBTEMPF','HOURLYPrecip'])


# In[ ]:


weatherData['DATE'] = weatherData['DATE'].apply(pd.to_datetime)


# The unique values here show that there might be some suspect data. (See issue 21 for details)

# In[ ]:


weatherData.iloc[:,2].unique()


# Creating a custom function to convert the values to numbers. `pd.to_numeric()` might work, but would prefer to convert the 'T' to a 0.001 to indicate trace amounts of precipitation. Also, values with an s would be converted to non-numeric.

# In[ ]:


def precipConvert(val):
    if str(val)[-1] == 's':
        return float(val[:-1])
    elif val == 'T':
        return 0.001
    else:
        return val


# testing custom function

# In[ ]:


testList = ['0.32s','T',0.32,np.nan]
for val in testList:
    print precipConvert(val)
    print type(precipConvert(val))


# In[ ]:


weatherData['HOURLYPrecip'].apply(precipConvert).apply(pd.to_numeric).unique()


# The temperatures here seem to be ok without transformation.

# In[ ]:


weatherData['HOURLYWETBULBTEMPF'].unique()


# Testing correlative data with bokeh example code.
# from http://bokeh.pydata.org/en/0.11.1/docs/user_guide/quickstart.html

# In[ ]:


from bokeh.plotting import figure, output_file, show, output_notebook


# In[ ]:


weatherDates = np.array(weatherData['DATE'], dtype=np.datetime64)
gateDates = np.array(gateCounts['Date'], dtype=np.datetime64)


# In[ ]:


window_size = 30
window = np.ones(window_size)/float(window_size)


# In[ ]:


#output_file("library_weather.html", title="Weather and Gate Counts in Jackson Library")
output_notebook()
p = figure(width=800, height=350, x_axis_type="datetime")


# In[ ]:


precipFormatted = weatherData['HOURLYPrecip'].apply(precipConvert).apply(pd.to_numeric)


# In[ ]:


p.line(weatherDates,weatherData['HOURLYWETBULBTEMPF'].values * 100,legend='Temp in F')
p.circle(weatherDates,precipFormatted * 1000,color='blue',alpha=0.2, legend='Precipitation')
p.circle(gateDates, gateCounts['Patrons'].values, color='red', legend='Gate Count')


#p.title = "Library Gate Counts vs. Weather"
p.legend.location = "top_left"
p.grid.grid_line_alpha=0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Gate Count'
p.ygrid.band_fill_color="gray"
p.ygrid.band_fill_alpha = 0.1


# This graph is not formatted correctly, but it does show how the functionality might work.

# In[ ]:


show(p)

