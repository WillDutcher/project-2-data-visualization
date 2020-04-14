import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Show header data.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows, rain = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        precipitation = float(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        rain.append(precipitation)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
ax.plot(dates, rain, c='pink', alpha=0.7)

# Format plot.
# ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Temperature (F)', fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_title("Daily Rainfall - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (in)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# print(highs)

# print(sorted(highs))
# print(sorted(highs, reverse=True))
