
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


# The Bokeh libraries necessary for this graph:

# In[ ]:

from bokeh.layouts import row, column
from bokeh.models import BoxSelectTool, LassoSelectTool, Spacer, FuncTickFormatter, FixedTicker, HoverTool, ColumnDataSource
from bokeh.plotting import figure, output_file, output_notebook, show, save
output_notebook()


# This is a grouping of the library data by average per hour over the entire dataset. 

# In[ ]:

libraryMeans = libraryData.groupby(libraryData.index.hour).mean()*100


# Since the format is a 24 (hours) x 312 (computers) matrix, and the scatter plot is looking for single-dimension arrays, the data needs to be unstacked into these arrays.

# In[ ]:

meansUnstacked = libraryMeans.unstack().reset_index()
meansUnstacked.columns = ["comps","hour","means"]


# In[ ]:

meansUnstacked.head()


# In[ ]:

comps = libraryMeans.unstack().reset_index().iloc[:,0].values
hours = libraryMeans.unstack().reset_index().iloc[:,1].values
means = libraryMeans.unstack().reset_index().iloc[:,2].values
print comps.size
print 24 * 312


# In[ ]:

print libraryMeans.index


# In[ ]:

print libraryMeans.columns


# Bokeh allows a number of tools included in the tool bar adjacent to the graph. Testing the tools available and configurations for each.

# In[ ]:

hover = HoverTool(
    tooltips=[
        ("Computer", "@comps"),
        ("Hour", "$y{0}:00"),
        ("Pct Use","@means")
    ],
    formatters={"Hour":"datetime"}
)

source = ColumnDataSource.from_df(meansUnstacked)

#TOOLS=[hover,"crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"]
TOOLS=[hover,"crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,reset,tap,save,box_select,poly_select,lasso_select"]


# In[ ]:

mainGraph = figure(tools=TOOLS, plot_width=900, plot_height=600,
                     min_border=10, min_border_left=50,
                     toolbar_location="above",
                     x_axis_location=None,
                     #y_axis_location=None,
                     title="Library Usage: Average Percent Utilization per Hour")
mainGraph.background_fill_color = "#fafafa"
mainGraph.select(BoxSelectTool).select_every_mousemove = False
mainGraph.select(LassoSelectTool).select_every_mousemove = False

def hourTicks():
    [str(i)+":00" for i in range(0,24)]

mainGraph.yaxis.formatter = FuncTickFormatter(code="""return Math.floor(tick)+':00'""")
mainGraph.yaxis.ticker = FixedTicker(ticks = range(0,24))

mainGraph.scatter("index","hour",radius="means",color="blue",alpha=.5,source=source)
output_file("./AvgPercentUtil.html", title='Library Usage: Average Percent Utilization per Hour')
show(mainGraph)

