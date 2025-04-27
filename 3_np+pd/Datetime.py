# from datetime import datetime, date, timedelta
import datetime as dt
'''
date = datetime.now()
print(date)
print(date.strftime("%H-%M-%S"))
'''
'''
date1= dt.date(2024,3,19)
date2= dt.date(2024,11,5)
print(date1, date2)
print("Verschil tussen de data: ", (date2-date1))
print("Verschil tussen de data: ", (date2-date1).days // 7)
'''
'''
# Oefen timedelta
#
'''

'''
import calendar as cal
print(cal.month(2025,3))
print(cal.calendar(2026))
'''
'''
# Wanneer valt volgende maandag?
dag_vandaag = dt.date.today().weekday()
print(dag_vandaag)
dagen_tot_maandag = (7 - dag_vandaag%7)
dagen_tot_maandag = 7 if dagen_tot_maandag==0 else dagen_tot_maandag
print("Dagen tot maandag: ", dagen_tot_maandag)
'''
'''
import time
for _ in range(10,0,-1):
    time.sleep(1)
    print(_)
'''
'''
import time
import datetime as dt
while True:
    print(dt.datetime.now().strftime("%Y:%H:%S"))
    time.sleep(1)
'''
'''
# Onbekend wat volgende manier oplost. Misschien gek teken voor de datum zoals Bjorn kreeg
import time
import datetime as dt
while True:
    # print(dt.datetime.now().strftime("%Y:%H:%S"))
    time.sleep(1)
    print("\r" + dt.datetime.now().strftime("%H:%M:%S"), end="", flush=True)
print()
'''
'''
import datetime as dt
import locale
locale.setlocale(locale.LC_TIME, "de_CH") #fr_BE, nl_BE, nl_NL, de_DE, de_CH
datumvector = ["10-03-2024", "8-04-2024", "12-07-2024"]
datumvector_date = []
fmt = "%d-%m-%Y"
for datum in datumvector:
     datum_as_date = dt.datetime.strptime(datum, fmt).strftime("%Y-%B-%d")
     datumvector_date.append(datum_as_date)
for _ in datumvector_date:
    print(_)
print()
# De methode werkt niet op een vector: "strptime() argument 1 must be str, not list"
# datumvector_date2 = dt.datetime.strptime(datumvector, fmt).strftime("%Y-%B-%d")
" Kan wel via list comprehension"
datumvector_date3 = [dt.datetime.strptime(datum, fmt).strftime("%Y-%B-%d") for datum in datumvector]
print(datumvector_date3)
'''
import datetime as dt
import locale
import pandas as pd
locale.setlocale(locale.LC_TIME, "de_CH") #fr_BE, nl_BE, nl_NL, de_DE, de_CH
fmt = "%d-%m-%Y"
datumvector = ["10-03-2024", "8-04-2024", "12-07-2024"]
df =pd.DataFrame(datumvector, columns=["Datum"])
# df["Datum"] = pd.to_datetime(df["Datum"])
df["Datum"] = pd.to_datetime(df["Datum"], format=fmt) # met format-string
df["Maand"] = df["Datum"].dt.month
df["Datum"].dt.tz_localize('utc') 
df["Datum"].dt.strftime("%d-%B-%Y") # Geen error, maar ook geen resultaat
print(df["Datum"])
for i in df["Datum"]:
    print(i.strftime("%d-%B-%Y"))
print()

# ToDo: localize / format datetime in pandas
#fmt = "%d-%m-%Y"
# dt.datetime.strptime(datum, fmt).strftime("%Y-%B-%d")

