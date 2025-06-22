import datetime
from pandas import Timestamp as pd_timestamp

def get_now(freq = '1h'):
    # Show the moment that is clicked in status label
    now = datetime.datetime.now()
    pd_now = pd_timestamp(now)
    pd_round = pd_now.round(freq)
    now_rounded = pd_round.to_pydatetime()
    return now_rounded

now_ = get_now()
print(f"Nu is {now_}")

t_array = [i * 0.01 for i in range(int((10 / 0.01 + 1)))]

# Create a list to store the new datetime objects
datetime_list = []

for t in t_array:
    # Create a new datetime object with the updated minute value
    # Change remainder (non-int) to seconds and microseconds
    remainder = (t%1*60)
    seconds = int(remainder)
    microseconds = int(remainder%1*1000000)
    print(f"seconds {seconds} microseconds {microseconds} ")


    new_datetime = now_.replace(minute=int(t), second= seconds, microsecond= microseconds)
    datetime_list.append(new_datetime)

print("datetime_list:", datetime_list)
