
import pandas as pd 
import numpy as np 



df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods = 20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South'] * 5,
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Recp': ['John', 'Mary', 'Bob', 'Alice'] * 5
})

df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

print(f'\n\n{df}\n\n')

pivot_1 = df.pivot_table(values = ['Sales', 'Units'], index = 'Region', columns = 'Product', aggfunc = 'median')
pivot_2 = df.pivot_table(values = ['Sales', 'Units'], index = 'Region', columns = 'Product', aggfunc = 'mean')

print(f'\n\nPivot Table # 1\n\n{pivot_1}\n\n')
print(f'\n\nPivot Table # 2\n\n{pivot_2}\n\n')


print(pd.crosstab(df['Region'], df['Product']))








