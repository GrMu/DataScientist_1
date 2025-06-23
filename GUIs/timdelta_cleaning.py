import pandas as pd

# Example Timedelta value
time_deviation = pd.Timedelta('0 days 00:00:07.270738088')

# Remove microseconds by flooring to the nearest second
time_deviation_no_microseconds = time_deviation.floor('s')

# Extract the components
components = time_deviation_no_microseconds.components

# Create a new Timedelta without the days
time_deviation_no_days = pd.Timedelta(hours=components.hours, minutes=components.minutes, seconds=components.seconds)

print(time_deviation_no_days)

if components.days == 0:
    timedelta_string = f"{components.hours:02}:{components.minutes:02}:{components.seconds:02}"
else:
    timedelta_string = str(time_deviation_no_days)
print("timedelta_string: ", timedelta_string)


# Timedelta representing 1 minute
one_minute = pd.Timedelta(minutes=1)

# Check if time_deviation is less than 1 minute
is_less_than_one_minute = time_deviation < one_minute

print(is_less_than_one_minute)
