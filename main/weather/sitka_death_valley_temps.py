import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_sitka = 'data/sitka_weather_2018_simple.csv'
filename_death_valley = 'data/death_valley_2018_simple.csv'
station_s = ''
station_dv = ''

with open(filename_sitka) as fs:
    with open(filename_death_valley) as fdv:
        sitka_reader = csv.reader(fs)
        sitka_header_row = next(sitka_reader)
        dv_reader = csv.reader(fdv)
        dv_header_row = next(dv_reader)

        # Show header data.
        for index, column_header in enumerate(sitka_header_row):
            print(index, column_header)
        for index, column_header in enumerate(dv_header_row):
            print(index, column_header)

        # Get dates and high/low temperatures from these files.
        dates, s_highs, s_lows, dv_highs, dv_lows = [], [], [], [], []
        for row in sitka_reader:
            station_s = str(row[0])
            current_date_s = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                s_high = int(row[5])
                s_low = int(row[6])
            except ValueError:
                print(f"Missing Sitka data for {current_date}.")
            else:
                dates.append(current_date_s)
                s_highs.append(s_high)
                s_lows.append(s_low)
        for row in dv_reader:
            station_dv = str(row[0])
            current_date_dv = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                dv_high = int(row[4])
                dv_low = int(row[5])
            except ValueError:
                print(f"Missing Death Valley data for {current_date_dv}.")
            else:
                dv_highs.append(dv_high)
                dv_lows.append(dv_low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, s_highs, c=('#910000'), alpha=0.5)
ax.plot(dates, dv_highs, c=('#00098a'), alpha=0.5)
ax.plot(dates, s_lows, c=('#e00202'), alpha=0.5)
ax.plot(dates, dv_lows, c=('#0211e0'), alpha=0.5)
ax.fill_between(dates, dv_highs, dv_lows, facecolor='#949bff', alpha=0.25)
ax.fill_between(dates, s_highs, s_lows, facecolor='#ff94b4', alpha=0.25)
ax.fill_between(dates, dv_lows, s_highs, facecolor='#40e371', alpha=0.25)

# Format plot.
title = f"Daily highs and lows - 2018\nComparison: {station_s} vs {station_dv}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°F)', fontsize=16)
ax.tick_params(axis='both', which='both', labelsize=16)

plt.savefig(f'temps_comparison_{station_s}_vs_{station_dv}_2018',
    bbox_inches='tight')
plt.show()
print(station_s)
print(station_dv)
