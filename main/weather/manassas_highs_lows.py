import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/manassas_weather_2019_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-pastel')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.4)
ax.plot(dates, lows, c='blue', alpha=0.4)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

# Format plot.
title = "Daily high and low temperatures - 2019\nManassas, VA"
ax.set_xlabel('Dates', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('manassas_temps_2019.png', bbox_inches='tight')
plt.show()

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
