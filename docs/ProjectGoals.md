# Project Goals

## To Do list

This list is by no means complete.  Items occur in order of dependence on
previous items.

1. Model system (including data types - for example the timestamp for computers should be compatible with the timestamp for any weather event, that is there must be a conversion in place to compare them)
2. Organize all data into a database system (should agree on constraints for this).
    * sqlite would likely be a good candidate for this, since it is a small
	  non-invasive dependency, and Python ships with sqlite support out of the
	  box.

## Overall goal
- Allow the user to query the system on information regarding our data and its interactions without having to write new functions every time: Recommend having functions whose names are agreed on and stored in a file somewhere so that we don't all create different ones for the same purpose
- Put weather data, computer data, schedule data in tables: To this end modeling our system with a simple diagram should be a high priority at the early stage
- Should allow ability to update/remove data from tables
- Store information collected in a simple to access format (i.e. put it in a table or file somewhere, don't want to have to comb through the pynotebook every time we want something)


## Coding Standards
### Determine conventions for code
##### Tasks:
- The variables should have a uniform set of naming conventions
- Creation of new objects/variables should be informative without being verbose
- other team members should be able to tell the purpose from its name.

## Datasets
### Library Data
#### The Library Data is in the following format:
`machineID, stateID, lastChanged`

This is:
- machine (by ID, foreign key in table for machine name)
- state (by ID, foreign key in table for state name)
- lastChanged (time/datestamp of state change occurrence)

#### Issues: While compact/simple, this presents a number of problems.
 - the data for all machines, and areas, are in a single table.
 - the data does not have a mechanism for time elapsed in individual states.
 - without a transformation, it is difficult to compare usage states to duration.
 - if table is transformed/expanded to give minutes in use per hour, it will be enormous.

##### Tasks:
 - find method for expanding data efficiently
 - enumerate additional comparison data for machines (e.g. location, monitor configuration, availability/hours)

### Weather Data
#### Issues: The weather data is in a verbose format

- The data in the weather extract is very expansive.
- This will require some editing to get the data to a usable state.

##### Tasks:
- determine what data is useful and isolate it.
- figure out a way to bring the two (or more) sets together
