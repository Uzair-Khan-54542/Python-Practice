
import pandas as pd 
import numpy as np 



df = pd.DataFrame({
    'names': ['Khan', 'Junejo', 'Kalia', np.nan, 'Gullu', 'Mona', 'Kashi'],
    'ages': [22, 20, 21, np.nan, 24, np.nan, 30],
    'cities': [np.nan, 'Lahore', 'Mansehra', 'Kiranchi', np.nan, 'Sialkot', np.nan]
})

print(df, '\n')

# print(df.isna().sum(), '\n')

# print(df.fillna('(empty)'))

# print(df.dropna(thresh = 3))

# values = [df['names'].mode(), df['ages'].mean(), df['cities'].mode()]
# df.fillna(value = values)

# print(df, '\n')


