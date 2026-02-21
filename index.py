
import pandas as pd 
import numpy as np 



data = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['s1', 's1', 's2', 's2', 's1', 's2', 's2', 's1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods = 8)
})


print(f'\n{data}\n\n')

# cat = data.groupby(['Category', 'Store'])[['Sales', 'Quantity']].mean()
# print(f'\n{cat}\n\n')

# Aggregation Function


print(data['Sales'].agg(['mean', 'median', 'count', 'min', 'max', 'std', 'sum']))






