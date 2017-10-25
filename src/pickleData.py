import LibDataImport
import weather
import glob
import os.path
import cPickle
import pandas as pd

# Load utilization summary data into a DataFrame, one column per computer.
files = glob.glob(os.path.join('..', 'data', 'LibCSV', '') + '*.csv')
machineStates = pd.concat([ pd.read_csv(fp, names=['machineName', 'state', 'datestamp']) for fp in files ], axis='index')
machineStates['datestamp'] = machineStates['datestamp'].apply(pd.to_datetime)
# Reformat the data to fulfill preconditions required by LibDataImport.machineStatesToPercentUtilization()
machineStates = machineStates[['machineName', 'datestamp', 'state']]
utilization = LibDataImport.machineStatesToPercentUtilization(machineStates)

output = open(os.path.join('..', 'data', 'LibData.pkl'), 'wb')
cPickle.dump(utilization, output, cPickle.HIGHEST_PROTOCOL)
output.close()

files = [ os.path.join('..', 'data', x) for x in [ '1101311.csv', '1052640.csv' ] ]
weatherData = pd.concat([ weather.parseWeatherData(fp) for fp in files ], axis='index')
output = open(os.path.join('..', 'data', 'WeatherData.pkl'), 'wb')
cPickle.dump(weatherData, output, cPickle.HIGHEST_PROTOCOL)
output.close()
