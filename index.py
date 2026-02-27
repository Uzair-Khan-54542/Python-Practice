
import numpy as np 
import pandas as pd 
import time


df = pd.read_csv('Countries.csv')

# Highest population country
country_with_the_highest_population_table_index = (df['population'] == df['population'].max()).idxmax()
country_with_the_highest_population = df.loc[country_with_the_highest_population_table_index]['country']

# Highest population country's capital
capital_of_the_country_with_the_highest_population = df.loc[country_with_the_highest_population_table_index]['capital_city']

# Least population country
country_with_the_least_population_table_index = (df['population'] == df['population'].min()).idxmax()
country_with_the_least_population = df.loc[country_with_the_least_population_table_index]['country']


# Least population country's capital
capital_of_the_country_with_the_least_population = df.loc[country_with_the_least_population_table_index]['capital_city']

# Top5 countries with highest democratic score
top_5_countries_with_highest_democratic_score_table_index = df['democracy_score'].nlargest(5).index
top_5_countries_with_highest_democratic_score = df.loc[top_5_countries_with_highest_democratic_score_table_index]['country']


# Counting total number of regions
total_count_of_regions = df['region'].nunique()


# Counting total number of countries who lie in eastern europe
countries_in_eastern_europe = df[df['region'] == 'Eastern Europe']['country']
countries_in_eastern_europe_count = countries_in_eastern_europe.count()

# 2nd highest populated country's leader
temp = df['population'].nlargest(2).index
second_most_populated_country_leader = df.loc[temp[-1]]['political_leader']


# Countries with unknown political leaders
countries_with_unknown_leaders = df[df['political_leader'].isna()]['country']
countries_with_unknown_leaders_count = (df['political_leader'].isna()).sum()
countries_with_unknown_leaders = list(countries_with_unknown_leaders)

# Counting the number of countries who have republic in their name
countries_containing_republic_in_their_names = df[df['country_long'].str.contains('republic', case = False,na = False)].shape[0]


# Name of the country in African region who has the highest population
# african_region_countries = df[df['region'].str.contains('africa', case = False, na = False)]['country']
african_region_countries = np.where(df['region'].str.contains('africa', case = False, na = False))

location = df.loc[african_region_countries]['population'].idxmax()
country_in_africa_region_with_the_highest_population = df.loc[location]['country']







# print(f'Country with the highest population = {country_with_the_highest_population}\n')

# print(f'Capital of the country with the highest population = {capital_of_the_country_with_the_highest_population}\n')

# print(f'Country with the least population = {country_with_the_least_population}\n')

# print(f'Capital of the country with the least population = {capital_of_the_country_with_the_least_population}\n')

# print(f'Top 5 highest democary score countries are: \n{top_5_countries_with_highest_democratic_score}\n')

# print(f'Total number of regions: {total_count_of_regions}\n')

# print(f'\n***** (Country names) *****\n\nCountries in Eastern Europe: \n{countries_in_eastern_europe}\n')
# print(f'***** (Country count) *****\n\nTotal countries in Eastern Europe: {countries_in_eastern_europe_count}\n')

# print(f'Leader of the second most populated country: {second_most_populated_country_leader}\n')

# print(f'Countries with unknown leaders are:\n{countries_with_unknown_leaders}\n\n')
# print(f'Count of countries with unknown leaders are:\n{countries_with_unknown_leaders_count}\n\n')

# print(f'countries containing republic in their names:\n{countries_containing_republic_in_their_names}')

# print(f'Country in African region with the highest population: {country_in_africa_region_with_the_highest_population}\n')

# print(df.info())



# print(df, '\n')