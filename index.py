
import pandas as pd 
import numpy as np 



df = pd.DataFrame({
    'names': ['Khan', 'Junejo', 'Kalia', np.nan, 'Gullu', 'Mona', 'Kashi'],
    'ages': [22, 20, 21, np.nan, 24, np.nan, 30],
    'cities': [np.nan, 'Lahore', 'Mansehra', 'Kiranchi', np.nan, 'Sialkot', np.nan]
})

# print(df, '\n')

# print(df.isna().sum(), '\n')

# print(df.fillna('(empty)'))

# print(df.dropna(thresh = 3))

# values = [df['names'].mode(), df['ages'].mean(), df['cities'].mode()]
# df.fillna(value = values)

# print(df, '\n')




# celebrities = pd.DataFrame({
#     'celebrity_id': [1, 2, 3, 4, 5],
#     'name': ['Kashi', 'Mana', 'Kalia', 'Billa', 'Jeda'],
#     'city': ['Mansehra', 'Peshawar', 'Karachi', 'Multan', 'Lahore']
# })

# net_worth = pd.DataFrame({
#     'celebrity_id': [1, 2, 3, 8, 5],
#     'networth': [20000000, 45000000, 1800000, 9000000000, 990000000000],
# })

# print(celebrities, '\n\n', net_worth, '\n')

# print(pd.merge(celebrities, net_worth, on = 'celebrity_id', how = 'outer'))
# print(pd.concat([celebrities, net_worth]))

# col_1 = pd.DataFrame({
#     'age': [12, 15, 14, 12, 11, 13]
# }, index = [0, 1, 2, 3, 4, 5])

# col_2 = pd.DataFrame({
#     'salary': [15000000, 20000000, 160000000, 158000000, 100000000, 2500000000]
# }, index = [3, 4, 5, 6, 7, 8])


# print(col_1.join(col_2))






