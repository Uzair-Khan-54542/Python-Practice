

import numpy as np 
import pandas as pd 
from datetime import datetime
import time 
from dateutil.relativedelta import relativedelta

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


def extract_timestamp(txt):

    start = txt.find(')')
    duration = ""
    for i in range(start + 1, start + 20):

        duration += txt[i]
    
    return duration

data['Total Time'] = data['Title'].apply(extract_timestamp)




def extract_duration(txt):

    start_str, end_str = txt.split(" - ")

    start_date = datetime.strptime(start_str, '%b %Y')
    end_date = datetime.strptime(end_str, '%b %Y')
    r = relativedelta(end_date, start_date)
    return r.years * 12 + r.months + 1

    # return (end_date - start_date).days

data['Duration(Months)'] = data['Total Time'].apply(extract_duration)





# print(data.loc[0]['Title'])
print(data.head(), '\n')
# print(data['Duration'].dtype, '\n')
# print(data, '\n')