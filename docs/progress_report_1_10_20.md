+ Nickolas Lloyd
    * Target goals:
        - Investigate possible relations between weather and computer usage patterns.
    * Achieved goals / activities:
        - 2017-10-10: Corrected and optimized data reshaping method.  Did direct
          comparison of old and new method, showing discrepencies in data and
          improved speed.  10h.
            + [LibDataImport.py](../src/LibDataImport.py)
            + [UsageVsWeather.ipynb](../src/UsageVsWeather.ipynb)
        - 2017-10-13: Demonstrate possible effect of outdoor temperature on
          overall computer usage.  4h.
            + [UsageVsWeather.ipynb](../src/UsageVsWeather.ipynb)
        - 2017-10-13: Show lack of effect of temperature on usage of individual
          computers.  2h.
            + [UsageVsWeather.ipynb](../src/UsageVsWeather.ipynb)
        - 2017-10-18: Improve presentation of plots and data relating
          temperature and usage.  2h.
            + [UsageVsWeather.ipynb](../src/UsageVsWeather.ipynb)


+ Michael Ellis
    * Target Goals
         - Determine whether computer usage is correlated with university scheduling, equipment configuration, location, and weather.
        - My tasks for the project thus far related to the weather data realm and attributing aspects. These included, cleaning up the weather data and translating the weather and sky condition metar codes. 
    * Achieved Goals / activities
        - 10/11/17: Attempted to remove characters from the sky and weather conditions data that were causing errors when trying to translate. This task relates to my goals because it prepares and cleans the data to be used in future translations of the code. Hours worked: approx. 3 hours
        - 10/13/17: Continued work on error codes and was successful in fixing the errors with translation of the sample sky conditions data. This task relates to my goals because it fine tuned my cleaning and errors in order to allow for proper translation. Hours worked: approx. 3 hours
        - 10/15/17 & 10/16/17: Discovered and fixed an error where the sky conditions translated data was off. The elevation calculations done during translation were much higher than they actually were. These tasks related to my goals because it fixed calculation errors caused during translation to allow me to present correct elevation in sky conditions. Hours worked: approx. 4.5 hours between both days
        - 10/18/17: A ’s’ character was brought to my attention from the LCD document, where some data may be suspect due to being manually entered in, this data was skipped during translation until we further decide on what to do with the weather data after some findings Nick discovered. This task relates to my goals because it allowed me to discover another character that makes some of the data suspect. This data was removed during translation, and as a result all sky and weather codes are now translated for use once we determine whether or not we will incorporate weather data. Hours worked: approx. 2.5 hours
        - 10/19/17: Prepared the files for merging with develop branch, resolve conflicts, and merge. This task relates to my goals because it allowed me to prepare my files in order to merge them to master. Hours worked: approx. 30 minutes
https://github.com/UNCG-CSE/Library-Computer-Usage-Analysis/blob/ellis/src/GSOWeatherParseTest.ipynb
https://github.com/UNCG-CSE/Library-Computer-Usage-Analysis/blob/ellis/src/GSOWeatherParseTest.py

+ Patricia Tanzer
   * Target Goals
      - Visualize some of the weather data into graphs
      - Begin documentation for the next presentation in a .docx file
   * Achieved Goals
      - made two new graphs in src/GSOWeather.ipynb. 
      - created .docx document anaylzing one of our original theories
   * Next Goals
      - update presentation document with analysis of work currently in master
      
+ Brown Biggers
	* Target Goals
		- Acquire datasets from multiple sources (Library, NOAA)
		- Create initial presentation files.
		- Determine Pandas versus NumPy processing methods/functions for tabular data processing
		- Research NOAA code designations for data import
		- Assess visualization/processing methods for weather and library gate count 
	* Achieved Goals
		- Datasets have been acquired in stages. Initially the goal was to provide enough data for testing. This is complete. Once the methods had been determined, larger datasets were acquired and uploaded. These datasets may require further processing and concatenation due to their size. Some of this data did not exist (e.g. computer attributes) and needed to be collected manually. Other datasets required processing (e.g. Library Gate Counts) as it was not in a consistent format.
			- Relevant Files:
				- (NOAA): [1052640.csv](../data/1052640.csv)
				- (NOAA): [1101311.csv](../data/1101311.csv)
				- (Library): [FullGateCounts.csv](../data/FullGateCounts.csv)
				- (Library): [computerAttributes.csv](../data/computerAttributes.csv)
				- (Library): [LibCSV](../data/LibCSV)
		- After working with an number of Pandas default functions, it appears that there will be a number of these that will suit our needs. There are still more that may show potential, and will require further research.
			- Relevant Files:	
      			- [GSOWeather.ipynb](../src/GSOWeather.ipynb)
				- [LibraryData.ipynb](../src/LibraryData.ipynb)
				- [LibraryGateCounts.ipynb](../src/LibraryGateCounts.ipynb)
				- [TimeTesting-Resample.ipynb](../src/TimeTesting-Resample.ipynb)
		- NOAA encoding shows some inconsistent tagging with regard to letter codes. We feel we have done what is necessary to assess the codes found in the imported datasets.
	* Next Goals
		- Work with the Bokeh library for dynamic visualization
		- Further research into statistical analysis and Pandas functionality to further refine the datasets, and determine what can be culled from inclusion.      
