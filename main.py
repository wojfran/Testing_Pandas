import pandas as pd

# testing loading csv files
data = pd.read_csv('pokemon_data.csv')

# reading data
# reading headers
print(data.columns)
# reading columns
print(data['Name'])
print(data['Name'][0:10])
# reading rows
print(data.head(5))
print(data.iloc[56:58])
# reading specific position (row,col) here, the 666th pokemon is named Elgyem
print(data.iloc[666, 1])
# testing loops
for index, row in data.iterrows():
    if row['Legendary'] is True:
        print(index, row['Name'])
# and now doing it without using loops:
print(data.loc[data['Legendary']])
# or more accurately:
# print(data.loc[data['Legendary']]['Name'])

# sorting data
# sorting through pokemon by highest to lowest attack, defense and hp,
# the ascending variable determines whether the sorting is ascending or descending
print(data.sort_values(['Attack', 'Defense', 'HP'], ascending=(0, 0, 0))[['Name', 'Attack', 'Defense', 'HP']])

# editing data
# adding a new colum summing up each pokemon's primary stats
data['Total'] = data['Attack'] + data['Defense'] + data['HP']
print((data.sort_values(['Total'], ascending=0)).head(10))
# dropping a column
data = data.drop(columns=['Total'])
print(data.head(5))
# adding total column more efficiently and with more stats,
# the axis specifies whether we add horizontally or vertically
data['Total'] = data.iloc[:, 4:9].sum(axis=1)
print((data.sort_values(['Total'], ascending=0)).head(10))
# rearranging columns
cols = list(data.columns)
data = data[cols[0:4]+[cols[-1]]+cols[4:12]]
print(data.head(3))

# writing data (index is set to false in order not to write indexes into the files,
# in our case redundant as we have the pokedex numbers in the data
# data.to_csv('pokemon_edit.csv', index=False)

#filtering data
new_data = data.loc[(data['Type 1'] == 'Fire') & (data['Type 2'] == 'Dragon')]
new_data = new_data.reset_index()
print(new_data[['Name', 'Type 1', 'Type 2']])
# filtering by name, we dont want to see any mega pokemon evolutions,
# (~ serves as ! in panda)
print(data.loc[~data['Name'].str.contains('Mega')])

# conditional changes
data.loc[data['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
print(data)

# groupby testing
grouped = data.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
print(grouped[['Attack']])
# /\ basically works like SQL very cool