import numpy as np
import pandas as pd

def parseWeatherData(filePath):
    raw = pd.read_csv(filePath, low_memory=False)
    raw.rename(columns = {'REPORTTPYE':'REPORTTYPE'}, inplace=True)
    raw['DATE'] = raw['DATE'].apply(pd.to_datetime)
    raw.set_index('DATE', inplace=True)
    return raw

hourlyColumns = ['REPORTTYPE',
'HOURLYSKYCONDITIONS',
'HOURLYVISIBILITY',
'HOURLYPRSENTWEATHERTYPE',
'HOURLYWETBULBTEMPF',
'HOURLYDRYBULBTEMPF',
'HOURLYDewPointTempF',
'HOURLYRelativeHumidity',
'HOURLYWindSpeed',
'HOURLYWindDirection',
'HOURLYWindGustSpeed',
'HOURLYStationPressure',
'HOURLYPressureTendency',
'HOURLYPressureChange',
'HOURLYSeaLevelPressure',
'HOURLYPrecip',
'HOURLYAltimeterSetting']

def hourlyWeatherOnly(df):
    # Return only columns pertaining to hourly measurements.
    x = df.filter(items=hourlyColumns)
    # Remove records pertaining to start-of-day values.
    return x[x['REPORTTYPE'] != 'SOD']
