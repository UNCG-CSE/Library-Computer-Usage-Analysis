# Project Goals

## Coding Standards
### Determine conventions for code
#### Tasks:
- The variables should have a uniform set of naming conventions
- Creation of new objects/variables should be informative without being verbose
- other team members should be able to tell the purpose from its name.

## Datasets
### The library data is in the following format:

`machineName, state, lastChanged`

This is machine (by ID, look up table for name)
state (by ID, lookup table for state name)
lastChanged (time/datestamp of state change occurrence)

#### While compact, this presents a number of problems.
 - the data for all machines, and areas, are in a single table.
 - the data does not have a mechanism for time in individual states.
 - without a transformation, it is difficult to compare usage states to duration.
 - if table is transformed/expanded to give minutes in use per hour, it will be enormous.

 #### Tasks:
 - find method for expanding data efficiently
 - enumerate additional comparison data for machines

### The weather data is in a verbose format

The data in the weather extract is very expansive, and will require some editing to get the data to a usable state.

#### Tasks:
- determine what data is useful and isolate it.
- figure out a way to bring the two (or more) sets together
