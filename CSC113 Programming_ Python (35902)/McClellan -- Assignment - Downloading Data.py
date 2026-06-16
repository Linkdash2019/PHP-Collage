from pathlib import Path
import csv
import plotly.express as px

latitudes, longitudes = [], []

path = Path('.other/MODIS_C6_1_USA_contiguous_and_Hawaii_MCD14DL_NRT_2024338.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for row in reader:
    try:
        latitude = float(row[0])
        longitude = float(row[1])

    except ValueError:
        print(f"Missing data!")
        raise
    else:
        latitudes.append(latitude)
        longitudes.append(longitude)

fig = px.scatter_geo(lat = latitudes,
                     lon = longitudes,
                     ).update_traces(marker=dict(color='red'))

fig.update_layout(
    title = 'Fires in the USA<br>12/4/2024', # appears to use HTML
    geo_scope='north america',
    )
fig.show()