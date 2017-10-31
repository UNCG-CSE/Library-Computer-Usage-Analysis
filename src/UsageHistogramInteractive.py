
# coding: utf-8

# ### Usage Histogram Interactive Plot

# similar in usage to: https://github.com/bokeh/bokeh/blob/master/examples/app/selection_histogram.py

# In[ ]:

import pandas as pd
import numpy as np


# In[ ]:

import gzip
import pickle


# This is the library data processed in the percent usage per hour.

# In[ ]:

with gzip.open(r'../data/LibData.pkl.gz') as f:
    libraryData = pickle.load(f)


# The dates here show the data from 3/24/10 - 10/19/17

# In[ ]:

libraryData.info()


# This is a grouping of the library data by average per hour using arbitrary endpoints.

# In[ ]:

startDate = pd.to_datetime("2016-01-01")
endDate = pd.to_datetime("2017-12-31")
dateMask = (libraryData.index > startDate) & (libraryData.index < endDate)


# The computer attributes need to be loaded into a separate dataframe:

# In[ ]:

compAttrs = pd.read_csv(r'../data/computerAttributes.csv',header=0)


# In[ ]:

compAttrs.info()


# In[ ]:

booleanCols = ["requiresLogon",
               "isDesktop",
               "inJackson",
               "is245",
               "largeMonitor",
               "adjacentWindow",
               "collaborativeSpace",
               "roomIsolated",
               "inQuietArea"]


# Using the attributes from above as booleans, create a mask for the `compAttrs` dataframe, and return the names.

# In[ ]:

attrsNames = compAttrs[compAttrs.requiresLogon == True].computerName


# In[ ]:

libraryMeans = libraryData[dateMask].groupby(libraryData[dateMask].index.hour).mean()*100


# In[ ]:

libraryMeans.info()


# Since the format is a 24 (hours) x 312 (computers) matrix, and the scatter plot is looking for single-dimension arrays, the data needs to be unstacked into these arrays.

# In[ ]:

meansUnstacked = libraryMeans.unstack().reset_index()
meansUnstacked.columns = ["comps","hour","means"]


# In[ ]:

meansUnstackedMerged = meansUnstacked.merge(compAttrs, left_on='comps',right_on='computerName')


# Since the number of machines in the later graph might change, going ahead here and setting variables based on the count of machines returned in the dataframe above:

# In[ ]:

machineCount = meansUnstackedMerged.comps.unique().size
recordCount = meansUnstackedMerged.index.size
hourCount = 24


# The Bokeh libraries necessary for this graph:

# In[ ]:

from bokeh.layouts import row, column
from bokeh.models import BoxSelectTool, LassoSelectTool, Spacer, FuncTickFormatter, FixedTicker, HoverTool, ColumnDataSource
from bokeh.plotting import figure, output_file, output_notebook, show, save
output_notebook()


# Bokeh allows a number of tools included in the tool bar adjacent to the graph. Testing the tools available and configurations for each. Hover, in this case, uses the data from the ColumnDataSource to populate the tooltips.

# In[ ]:

hover = HoverTool(
    tooltips=[
        ("Computer", "@comps"),
        ("Hour", "$y{0}:00"),
        ("Pct Use","@means")
    ],
    formatters={"Hour":"datetime"}
)
#TOOLS=[hover,"crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"]
TOOLS=[hover,"crosshair,pan,wheel_zoom,box_zoom,reset,tap,save,box_select,poly_select,lasso_select"]


# This ColumnDataSource is necessary to pass the dataframe values to the scatter plot later.

# In[ ]:

source = ColumnDataSource.from_df(meansUnstackedMerged)


# These are the basic commands to create the graph known as `mainGraph`. The `select()` commands are perceived to improve performance on large datasets

# In[ ]:

mainGraph = figure(tools=TOOLS, plot_width=900, plot_height=600,
                     min_border=10, min_border_left=50,
                     toolbar_location="above",
                     x_axis_location=None, # this is left in, as the x-axis ticks are hard to read zoomed out.
                     #y_axis_location=None, 
                     title="Library Usage: Average Percent Utilization per Hour")
mainGraph.background_fill_color = "#fafafa"
mainGraph.select(BoxSelectTool).select_every_mousemove = False
mainGraph.select(LassoSelectTool).select_every_mousemove = False


# Formatting the tickers requires some finesse. This first example uses some JavaScript to format the tick values to a 24-hour clock, and then constrain it to integers.

# In[ ]:

mainGraph.yaxis.formatter = FuncTickFormatter(code="""return Math.floor(tick)+':00'""")
mainGraph.yaxis.ticker = FixedTicker(ticks = range(0,24))


# Formatting the xaxis requires aligning the computernames to the values within the unstacked dataframe. This is omitted for now. 

# In[ ]:

keys=range(0,recordCount,hourCount)
values=list(meansUnstackedMerged.comps.unique())
graphCompIndex = dict(zip(keys,values))
mainGraph.xaxis.ticker = FixedTicker(ticks = range(0,recordCount,hourCount))
mainGraph.xaxis.major_label_overrides = graphCompIndex


# In[ ]:

mainGraph.scatter("index","hour",radius="means",color="blue",alpha=.4,source=source)
#output_file("./AvgPercentUtil.html", title='Library Usage: Average Percent Utilization per Hour')
show(mainGraph)

