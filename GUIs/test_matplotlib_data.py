'''
Create data to plot
'''
import numpy as np
import pandas as pd

# Create some data
t_array = [i*0.01 for i in range(int((10/0.01+1)))]
y1 = [2 * np.sin(2 * np.pi * t) for t in t_array]
y2 = [2 * np.cos(2 * np.pi * t) for t in t_array]
y3 = [1+1 * np.sin(3 * np.pi * t) for t in t_array]
y4 = [0.5 + 1.5 * np.sin(4 * np.pi * t) for t in t_array]
y5 = [2 - 1* np.cos(2.5 * np.pi * t) for t in t_array]
y6 = [3 - 1.5 * np.sin(4 * np.pi * t) for t in t_array]
data_pd = pd.DataFrame({'t':t_array, 'y1':y1, 'y2': y2, 'y3': y3, 'y4':y4, 'y5':y5, 'y6':y6})
data_columns = list(data_pd.columns)


