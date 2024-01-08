# import panadas library 
import pandas as pd

# import numpy library
import numpy as np

# importing flights csv fils
flights = pd.read_csv("PythonZenva/DataManipulationPANDAS/PandasDataManip-CourseFiles/Completed - Course Files/flights.csv", index_col=False)

# sort_values allows you to sort by a specific column 

# flights sorted by distance
flight_distance_sorted = flights.sort_values(by = ["DISTANCE"])
print(flight_distance_sorted)

# you can specify the sort order by using ascending argument

# flights sorted by distance descending order
flight_distance_sorted = flights.sort_values(by = ['DISTANCE'], ascending = False)
print(flight_distance_sorted)

# sort the data by AIR_TIME values descending 

# flights sorted by air time descending order 
flight_airtime_sorted = flights.sort_values(by = ["AIR_TIME"], ascending = False)
print(flight_airtime_sorted)

# you can sort by multiple columns 

# flights sorted by distance and then by airtime 
flights_distance_airtime_sorted = flights.sort_values(by = ['DISTANCE', 'AIR_TIME'], ascending = False)
print(flights_distance_airtime_sorted) 

# all flights use a boolean to check values against, and will return all rows that satify that 
# expression. Consider the following example

# fetching all January flights
flight_Jan = flights['MONTH'] == 1
print(flight_Jan)

# this returns a list of whether or not the month column was equal to 1 if we wanted to filter the rows
# based on the condition we index the statement into flights 

# selecting for January flights 
flight_Jan = flights[flights['MONTH'] == 1] 
print(flight_Jan)

# filtering can also be done with string values 

# flights leaving from New York
flight_NY = flights[flights['ORIGIN_STATE_NM'] == 'New York']
print(flight_NY)

# flights can be filtered using comparison operators 

# flights longer than 4000 miles
long_flights = flights[flights["DISTANCE"] > 4000]
print(long_flights)

# multiple filters can be used to "refine" the data

# fetching all long flights leaving from hawaii
long_flights_HI = long_flights[long_flights["ORIGIN_STATE_NM"] == "Hawaii"]
print(long_flights_HI)

# when working with dataframe logical operators such as and or and not cannot be used. Instead we use
#   bitwise operators like & | and ~ when using bitwise operators the conditions must be wrapped in 
#   parantheses due to order of operations. Consider the following example

# all long flights that start OR end in Hawaii 
long_flights_HI = long_flights[(long_flights["ORIGIN_STATE_NM"] == "Hawaii") | (long_flights["DEST_STATE_NM"] == "Hawaii")]
print(long_flights_HI)

# notice that the list above is the same list as the long flights list

# fetching all flights more than 4,000 miles and in January
long_flights_Jan = flights[(flights['DISTANCE'] > 4000) & (flights['MONTH'] == 1)]
print(long_flights_Jan)

# fetching all flights more than 4,000 miles and NOT in January 
long_flights_NOT_Jan = flights[(flights['DISTANCE'] > 4000) & ~(flights['MONTH'] == 1)]
print(long_flights_NOT_Jan)

# data can be grouped using the groupby equation 

# flights grouped by month 
flights_by_month = flights.groupby("MONTH")
# print(flights_by_month)

# the above print function does not work because we have to specify the group we want

# fetching december flight group
print(flights_by_month.get_group(12))

# now say we want to know the total distance traveled by planes in each month. We start with our data
#   grouped by month, then specify the DISTANCE values, then call the .aggregate function. For its 
#   parameter we’ll enter a NumPy function which will calculate the sum total of all distances for each 
#   group.

# total distance traveled by planes in each month
total_month_distance = flights_by_month['DISTANCE'].aggregate(np.sum)
print(total_month_distance)

# fetching average distance of a flight per month 
mean_month_distance = flights_by_month['DISTANCE'].aggregate(np.mean)
print(mean_month_distance)

# fetching largest distance covered per month 
max_month_distance = flights_by_month['DISTANCE'].aggregate(np.max)
print(max_month_distance)

# fetching smallest distance covered per month
min_month_distance = flights_by_month['DISTANCE'].aggregate(np.min)
print(min_month_distance)

# 2e can also use groupby to quickly get important information

max_distance = flights_by_month['DISTANCE'].aggregate(np.sum).max()
print(max_distance) 

# we can retrieve index for that value by using idxmax()
max_distance_idx = flights_by_month['DISTANCE'].aggregate(np.sum).idxmax()
print(max_distance_idx)

# this works with minimum values 
min_distance = flights_by_month['DISTANCE'].aggregate(np.sum).min()
min_distance_idx = flights_by_month['DISTANCE'].aggregate(np.sum).idxmin()
print(min_distance)
print(min_distance_idx)

# fetching the number of cancelled flights per month
cancelled_flights_month = flights_by_month['CANCELLED'].aggregate(np.sum)
print(cancelled_flights_month)