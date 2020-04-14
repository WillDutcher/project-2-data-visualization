import csv
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore structure of the data.
csv_filename = 'data/world_fires_7_day.csv'
with open(csv_filename) as c_f:
    reader = csv.reader(c_f)
    header_row = next(reader)

    # Get data for plotting.
    lats, lons, brights = [], [], []
    counter = 0
    for row in reader:
        counter += 1
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except:
            # print(f"Missing info: {row[2]} doesn't compute for this map.")
            print("ERROR")
        else:
            if bright < 380:
                continue
            else:
                lats.append(lat)
                lons.append(lon)
                brights.append(bright)
    print(counter)
# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': brights,
    'marker': {
        'size': [bright/10 for bright in brights],
        'color': brights,
        'colorscale': 'Picnic',
        'reversescale': True,
        'colorbar': {
            'title': 'Brightness'
        },
    }
}]
my_layout = Layout(
    title='Fires from whenever this thing was recorded.'
)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
