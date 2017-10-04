import numpy as np
import pandas as pd

assert(np.__version__ > '1.12.1')
assert(pd.__version__ > '0.20.1')

def parseLibraryData(filePath):
    raw = pd.read_csv(filePath)
    raw['dateStamp'] = raw['dateStamp'].apply(pd.to_datetime)
    return raw
    

# Return library computer usage data as
#
# dateStamp | computer1 | computer2 | ... | computerN
# ----------+-----------+-----------+-----+----------
# H1        | minutes   | minutes   | ... | minutes
# H2
# ...
# Where H{1,2,...,N} are timestamps that occur every hour on the hour,
# computer{1,2,...,N} are the names of the computers in the library,
# and minutes is the number of minutes of usage of the given computer
# during the given hour.
def toHourlyUsage(df):
    # This is a matrix of the datestamp times as the index, computers as the
    # columns, and the state change at the intersection.
    fullMatrix = df.pivot(index='dateStamp',columns='computerName',values='state').sort_index()

    # This function converts the three off-states into a zero (0), and the
    # single on state ('in-use') into a one (1). The remainder are left as np.nan.

    # Note: cells formatted as integer do not support np.nan, so the cells are
    # converted to floats to accommodate it.
    def inUseConvert(state):
        offStates = ['available','restarted','offline']
        if state == 'in-use':
            return 1
        elif state in offStates:
            return 0
        else:
            return np.nan

    fullMatrixInts = fullMatrix.applymap(inUseConvert)
    return fullMatrixInts.ffill().resample('min').ffill().resample('H').sum()
