from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path1 = Path('.other/death_valley_2021_simple.csv')
path2 = Path('.other/sitka_weather_2021_simple.csv')
lines1 = path1.read_text().splitlines()
lines2 = path2.read_text().splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)
reader2 = csv.reader(lines2)
header_row2 = next(reader2)

# Extract dates, and high and low temperatures.
dates, highs1, lows1 = [], [], []
highs2, lows2 = [], []

for row1 in reader1:
    current_date = datetime.strptime(row1[2], '%Y-%m-%d')
    try:
        print(row1)
        high1 = int(row1[3])
        low1 = int(row1[4])

    except ValueError:
        print(f"Missing data for {current_date} in Death Valley")
    else:
        dates.append(current_date)
        highs1.append(high1)
        lows1.append(low1)


for row2 in reader2:
    current_date = datetime.strptime(row2[2], '%Y-%m-%d')
    try:
        print(row2)
        high2 = int(row2[4])
        low2 = int(row2[5])

    except ValueError:
        print(f"Missing data for {current_date} in Sitka")

    else:
        #dates.append(current_date)
        highs2.append(high2)
        lows2.append(low2)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs1, color='red', alpha=0.5)
ax.plot(dates, lows1, color='blue', alpha=0.5)
ax.plot(dates, highs2, color='orange', alpha=0.5)
ax.plot(dates, lows2, color='green', alpha=0.5)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nRed Blue = Death Valley\nOrange Green = Sitka"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()