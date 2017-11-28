# Library-Computer-Usage-Analysis

## Contributors: Brown Biggers, Michael Ellis, Nickolas Lloyd, Patricia Tanzer




## Goals: Establish which characteristics make a computer more likely to be used, including campus scheduling, equipment configuration, placement, population in the library, and area weather. Using this data, this project would like to use machine learning to determine the best placement of computers for future allocation, and possible reconfiguration of equipment and space.

### Suggested Reading Order: To get the highlights, look at the Presentation powerpoint (not yet available). 
#### For more detailed information and examples, begin with LibraryGateCounts. Move to UsageByMachine, then UsageVsGateCounts. Follow that with UsageVsWeather and WindowAndMonitorUsageCorrelations. Finally PredictUsageByAttributes finishes off the set.

## Src:

LibraryGateCounts: Shows the total population in Jackson library each day and its correlation to semester schedule, with initial relations of weather to gate counts.

UsageByMachine: Shows the total usage of each machine in Jackson Library by a percentage of each hour. Visualization shows that some regions are more heavily used than others, and at what times.

UsageVsGateCounts: Shows the correlations between gate counts and usage of each machine and region in Jackson Library. The results indicate that some regions, such as the Reading Room and Info Commons, are more popular than others. These areas share certain conditions unique from the 'unpopular' ones, such as natural light and dual monitors, which will be examined in the next set of notebooks.

UsageVsWeather: Shows the relation between total use of a given computer vs local temperature and rainfall, broken down by region. Results indicate that weather has no meaningful effect on computer use.

WindowAndMonitorUsageCorrelations: Shows that computers with dual monitors are used more heavily than those with only one from spring 2016 - fall 2017, and that a computer's adjacency to a window has no effect on computer use during the same period.

PredictUsageByAttributes: The creation and use of a model to take various attributes (such as number of monitors and location) and predict whether that machine will be a highly used machine or a lesser used one.

Weather.py: contains helper functions for working with weather.

## Data:

computerAttributes.csv: Each computer is tagged with a value for: dbID, computerName, requiresLogon, isDesktop, inJackson, location, is245, floor, numMonitors, largeMonitor, adjacentWindow, collaborativeSpace, roomIsolated, inQuietArea

FullGateCounts.csv: A 'gate count' is taken at the start and end of each day in Jackson library, which records the number of people who have passed through the gates. From this we can determine the daily population of the library.

LibraryGateCounts.csv: Gate counts for a single semester, used in example

LibData.pkl.gz: The compressed version of LibData.pkl, which records usage statistics for each computer.

WeatherDat.pkl.gz: The compressed version of WeatherData.pkl, which records NOAA's data about heat, precipitation, wind speeds, and other attributes hourly for several years at the Greensboro PTI airport.

semesters.csv: Lists the start and end date of each semester.

1052640.csv: One half of weather data converted to readable format.

1101311.csv: Other half of weather data converted to readable format.

