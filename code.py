# --------------
import pandas as pd 

# Read the data using pandas module.
ipldata = pd.read_csv(path)

# Find the list of unique cities where matches were played
unique_city = ipldata['city'].unique()
print("The Unique cities where IPL Matches played are\n",list(unique_city))
# Find the columns which contains null values if any ?
null_values = ipldata.isnull().sum()
print("The Columns with Null values are\n",list(null_values[null_values>0].index))
# List down top 5 most played venues
top_5_venues = ipldata.groupby(['venue'])[['match_code']].nunique().sort_values(by='match_code',ascending=False).head()
print("The Top 5 Venues are\n",list(top_5_venues.index))
# Make a runs count frequency table
runs_table = ipldata['runs'].value_counts()
print(runs_table)
# How many seasons were played and in which year they were played 
ipldata['year'] = ipldata['date'].str[:4]
print("The No of Seasons Played is\n",ipldata['year'].nunique())
# No. of matches played per season
matches_season = ipldata.groupby(['year'])['match_code'].nunique()
print("The No Matches Played in each season are\n",matches_season)
# Total runs across the seasons
total_runs = ipldata.groupby(['year'])['total'].sum()
print("the Total No of Runs in Each Season are\n",total_runs)
# Teams who have scored more than 200+ runs. Show the top 10 results
runs_scored = ipldata.groupby(['batting_team','match_code'])[['total']].sum()
top_10_results = print("The Top 10 Results for 200 Score are\n",runs_scored[runs_scored>200].dropna().sort_values(by='total',ascending=False).head(10))

# What are the chances of chasing 200+ target

# Which team has the highest win count in their respective seasons ?


