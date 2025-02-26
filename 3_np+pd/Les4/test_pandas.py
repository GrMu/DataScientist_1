import pandas as pd

'''
df = pd.DataFrame(
    {'indicator': ['indicator 1', 'indicator 1', 'indicator 2', 'indicator 2'],
     'year': [2014, 2014, 2015, 2015],
     'value type': ['upper', 'lower', 'upper', 'lower'],
     'value': [12.3, 10.2, 15.4, 13.2]
     },
    index=[1, 2, 3, 4])

# df['value'] = df.groupby('indicator')['value'].transform('mean')
df2 = df.groupby('indicator')['value'].mean()
print(df2)
'''
#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'position': ['G', 'F', 'F', 'G', 'F', 'F', 'G', 'G'],
                   'points': [30, 22, 19, 14, 14, 11, 20, 28],
                   'assists': [4, 3, 7, 7, 12, 15, 8, 4]})
print(df)
#calculate mean of points and mean of assists grouped by team
df2 = df.groupby('team')[['points', 'assists']].mean()
print(df2)