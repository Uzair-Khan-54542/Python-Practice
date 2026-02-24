

import numpy as np 
import pandas as pd 

data = pd.read_csv(r'c:\Users\user\Downloads\anime.csv')


# print(data.loc[1]['Title'])

def extract_episodes(title):

    episode = ""

    start = title.find('(')
    end = title.find(')')

    for i in range(start + 1, end):

        episode += title[i] 
    
    return episode


data['Episodes'] = data['Title'].apply(extract_episodes)        

data['Episodes'] = data['Episodes'].str.replace(' eps', '')

data['Episodes'] = data['Episodes'].astype(int)














# print(data.head())
# print(data, '\n')