
import pandas as pd

df = pd.read_csv('text_data.csv')
print(df.head(5)) #getting the first 5 rows.
print(df.tail(5)) #getting the last 5 rows.

# Reading the headers
print(df.columns)
df.columns
# get a specific column
print(df['Name'][0:5]) #top 5
print(df.iloc[1:4]) #iloc stands for index location
# to go through each row.
for index, row in df.interrows():
  print(index, row)
  print(index, row["Name"]) # display rows under Name column
  
df.loc[df['Type-1'] == 'Fire'] #looking for a column with only 'Fire'

# Describe displays all sort of info such as mean, average, std, 25%, 75%, min, max etc
df.describe()

# sorting values
df.sort_values('Name', ascending=False) #by name in this case

df.sort_values(['Type 1', 'HP'], ascending=True) #multiple sorts

#Making changes to the data.
# adding a new column 'Total', Adding the mentioned columns.
df['Total'] = df['HP'] + df['Attack']+ df['Defence']+ df['Sp. Atk']+ df['Sp. def']+ df['Speed']
# or
df['Total'] = df.iloc[:, 4:10].sum(axis=1) #axis 1 adds horizotally, axis 0 adds vertically.

print(df.head(5))

# Dropping a column.
df = df.drop(columns['Total'])




  


