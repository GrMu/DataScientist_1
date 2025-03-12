import numpy as np
import pandas as pd
data = {"tijd":[1,2,3,4,np.nan,6], "getallen":[1,2,np.nan,4,5,np.nan]}
print(data)
df=pd.DataFrame(data)
print(df)

df2=df.copy()
df2["getallen"]=df2["getallen"].fillna(method='ffill') #deprecated
print(df2)
df4=df.copy()
df4["getallen"]=df4["getallen"].ffill()
print(df4)

df3=df.copy()
df3["getallen"]=df3["getallen"].interpolate(method="linear")
print(df3)

df5=df.copy()
df5=df5.ffill()
print(df5)

df6=df.copy()
df6=df6.interpolate(method="linear")
print(df6)


