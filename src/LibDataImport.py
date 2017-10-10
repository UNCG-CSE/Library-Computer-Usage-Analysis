import pandas as pd
import numpy as np

from pandas.tseries.offsets import *
import functools
import itertools


def _concat(lists):
    #return functools.reduce(lambda x, y: x+y, lists, [])
    return itertools.chain(*lists)

# Compute the intervals during which each computer was in use.
#
# @df must be a pandas DataFrame with columns ['machineName', 'datestamp',
# 'state'].
#
# Returns a list of (machineName,[(timestamp,timerange)]) corresponding to
# sessions of machine usage.
def toUsageIntervals(df):
    # Bin records by `machineName'.
    names = df['machineName'].unique()
    grouped = df.sort_values(by='datestamp').groupby(by='machineName')
    binned = [(name, group.loc[:,'datestamp':'state']) for (name, group) in grouped]

    # This function helps f() construct a mask to collapse runs of in-use or
    # not-in-use records into a single row.
    def g(x, xs):
        if x == False:
            return [True] + xs[1:]
        else:
            return [True] + ([False] * (len(xs) - 1))

    def f(frame):
        # Mark which records correspond to 'in-use'.
        inUse = (frame['state'] == 'in-use').values
        grouped = itertools.groupby(inUse)
        # Filter down to those records which indicate 'in-use', or which occur
        # directly after such a record.
        mask = list(_concat([g(x,list(xs)) for (x,xs) in grouped]))
        # We only care about the datestamps of these transitions.
        filtered = frame[mask]['datestamp'].values
        # Modify the array to start with a login event.
        if inUse[0]==False:
            filtered = filtered[1:]
        # TODO: ensure that the last value of inUse is False.
        #
        # If the last record is a login event, then we don't know how long the
        # user stayed at the computer, so drop the record.
        if inUse[-1]==True:
            filtered = filtered[:-1]
        # Records correspond sequentially to login/logoff pairs, so zip the
        # datestamps (login, logoff) datestamp pairs.
        ranges = zip(filtered[0::2], filtered[1::2])
        return [(pd.Timestamp(x), pd.Timedelta(y-x)) for (x, y) in ranges]

    # Compute date ranges of usage for each machine.
    return [(name, f(frame)) for (name, frame) in binned]
    
# Convert date ranges into hourly usage data.
def usageIntervalsToPercentUtilization(binned, period='h'):
    # Declare this here to avoid with each call of dateRangeToPeriodUtilization().
    period_delta = pd.Timedelta(1, unit=period)
    def dateRangeToPeriodUtilization(begin, length):
        # Round the starting time down to the nearest period.
        start = begin.floor(period)
        endTime = begin + length
        lastPeriod = endTime.floor(period)
        if (lastPeriod == start):
            # If we don't cross a period boundary, just return the amount of
            # time spent 'in-use' for this period.
            return [(start, length)]
        else:
            # Otherwise, we need to break the session down by period, according
            # to wall-time.  We already have the beginning of this interval.
            # Round up the end time to the nearest period to get the end-point
            # of the interval.
            end = lastPeriod + period_delta
            # Now create a list of timestamps corresponding to periods on the
            # clock for this session.
            #
            # One would think 'closed=None' means don't include the first or
            # last value in the interval.  This doesn't seem to be the case
            # though, so manually remove those values.  Otherwise, we end up
            # with two copies of the start period, and two copies of the end
            # period.
            periods = list(pd.date_range(start, end, freq=period, closed=None)[1:-1])
            # Compute the amount of time spent 'in-use' in the first hour-long
            # interval.
            first = period_delta - (begin - start)
            # Similarly for the last hour-long interval.
            last = endTime - lastPeriod
            # Create a list of (timestamp,timerange) pairs giving the total
            # amount of time spent 'in-use' for each period-long interval.
            return zip([start] + periods, [first] + ([period_delta] * (len(periods) - 1)) + [last])

    def dateRangeToDataFrame(dateRanges):
        # Convert each date range into a list of (timestamp,timerange) where
        # each timestamp corresponds to the beginning of a period within the
        # timerange.
        if len(dateRanges)==0:
            return []
        next_ = _concat([dateRangeToPeriodUtilization(x, y) for (x, y) in dateRanges])
        # Group and sum times by period to remove duplicate periods, which would
        # happen if we have multiple timeranges within a period, e.g. if we have
        # two entries ('2017-08-31 09:02:00', '+00:05:00') and
        # ('2017-08-31 09:10:00', '+00:13:00').
        sorted_ = sorted(next_, key=lambda x: x[0])
        grouped = itertools.groupby(sorted_, key=lambda x: x[0])
        z = [(x, functools.reduce(lambda a, b: a + b, [y for (_, y) in w])) for (x, w) in grouped]
        # return a value of type [(timestamp, double)].
        return [(x, y / pd.Timedelta(1, unit=period)) for (x, y) in z]

    # utilization has type [(machineName, [(timestamp, double)])], where the
    # doubles correspond to percent utilization during the @period-long time
    # beginning at the timestamp.
    utilization = [(x, dateRangeToDataFrame(y)) for (x, y) in binned]
    # Get the unique list of timestamps in the data set.
    all_timestamps = _concat([[y for (y,_) in x] for (_,x) in utilization])
    unique_timestamps = set(all_timestamps)
    sorted_timestamps = sorted(unique_timestamps)
    # Create a zero entry for each unique timestamp to add to the data for each
    # computer.  This is to ensure that when assembling the final matrix, each
    # column has the same number of entries.
    zeros = [(x, 0.0) for x in sorted_timestamps]
    # Compute (machineName, [(timestamp, utilization)]).
    # `dict(zeros + y)' takes advantage of the fact that the dict() function
    # discards all but the last value associated with each repeated key in its
    # input list argument to set 0.0 as a default utilization for each time-slot
    # for which no data exists in @binned.
    uniquified = [(x, [z for (_,z) in sorted(dict(zeros + y).iteritems(), key=lambda v: v[0])]) for (x, y) in utilization]
    return pd.DataFrame(dict(uniquified), index=sorted_timestamps)


# @df must be a pandas DataFrame with columns ['machineName', 'datestamp',
# 'state'].
#
# Transforms @df into a new DataFrame with columns given by the values of the
# 'machineName' column of @df, rows indexed by hour, and values of percent
# utilization for the given machine during each hour.
def machineStatesToPercentUtilization(df):
    return usageIntervalsToPercentUtilization(toUsageIntervals(df), period='h').resample('H').asfreq().fillna(0)
