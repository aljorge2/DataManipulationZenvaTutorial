# importing pandas library 
# documentation for library can be found at https://pandas.pydata.org/ 
import pandas as pd


# importing numpy library
import numpy as np

# creating one column random data
df_data = {
'col1': np.random.rand(5)
}

# converting column to dataframe using pandas
df = pd.DataFrame(df_data)
print(df)

# creating 2 more columns
df_data = {
'col1': np.random.rand(5),
'col2': np.random.rand(5),
'col3': np.random.rand(5)  
}

# converting column to dataframe using pandas
df = pd.DataFrame(df_data)
print(df)

# printing first two rows dataframe
print(df[:2])

# printing first column information in dataframe
print(df['col1']) 

# selecting data multiple columns
print(df[['col1', 'col2']])

# import first sheet .xls file 
tracks = pd.read_excel("PythonZenva/DataManipulationPANDAS/PandasDataManip-CourseFiles/Completed - Course Files/Tracks.xls", sheet_name=0)

# printing dataframe
print(tracks)

# printing columns of dataframe
print(tracks.columns)

# printing milliseconds column of dataframe
print(tracks['Milliseconds'])

# reading flights csv not using 1st column as index
flights = pd.read_csv("PythonZenva/DataManipulationPANDAS/PandasDataManip-CourseFiles/Completed - Course Files/flights.csv", index_col=False)
print(flights)

# print column names of dataframe
flights.columns

# printing one column 
print(flights["DAY_OF_WEEK"])

# printing one column
print(flights["ORIGIN"])

print(flights[['ORIGIN', 'DEST']])

# selecting first three rows of dataframe
three_rows = flights[:3]
print(three_rows)

# iloc stands for integer location. when given a row and a column and it returns the single value at that intersection. The iloc object
#   only takes integer values, so the column must be an integer, not a string. When entering the indices, specify the row location first
#   and the column location second. The format is data.iloc[row, column]. REMEMBER THAT PYTHON USES 0 INDEXING

# printing first row and column in dataframe
print(flights.iloc[0,0])

# use iloc to fets 3 row second column

# print third row second column
print(flights.iloc[2,1])

# get_loc allows you to take a column name string and returns its index

# second row of day of month column
print(flights.iloc[2,flights.columns.get_loc('DAY_OF_MONTH')])

# first three row of day of month column 
print(flights.iloc[:3, flights.columns.get_loc("DAY_OF_MONTH")])

# getting origin and destination data from first flight (first row)
print(flights.iloc[0, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]])

# getting origin and destination data from first three flights 
print(flights.iloc[:3, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]]
)
