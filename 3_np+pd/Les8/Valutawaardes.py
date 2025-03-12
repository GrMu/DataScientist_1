import numpy as np
import pandas as pd
data = {"tijd":[1,2,3,4,5,6], "geld":["€1","€2","£3","$4","€5","$6"]}
print(data)
df=pd.DataFrame(data)
print(df)

df2=df.copy()
#df2["geld"]=df2["geld"].str.replace(r"[€$£]","") # Dit mag. '\D' is mooier:
df2["valuta"]=df2["geld"].str.extract(r"([\D])")
#df2["valuta"]=df2["geld"].str.extract(r"([$€£])")
df2["geld"]=df2["geld"].str.replace(r"([\D])","", regex=True).astype('int')
#df2["geld"]=df2["geld"].str.replace(r"([€£$])","", regex=True).astype('int')
print(df2)


