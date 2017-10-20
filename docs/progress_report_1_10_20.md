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

