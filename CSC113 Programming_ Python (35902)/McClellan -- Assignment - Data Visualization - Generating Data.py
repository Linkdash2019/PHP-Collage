import matplotlib.pyplot as plot
import requests
import time

year = '2021'
month = '11'
day = 1

high = []
low = []
print('Working... Please wait')
while day < 31:
    date = (year+'-'+month+'-'+f"{day:02d}")
    normal = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00026796&datatype=TMIN&datatype=TMAX&startdate='+date+'&enddate='+date+'&units=standard', headers={"token":"iaJCZkVywooFpyNRwIIsGuMcoMlzAWIa"})
    try:
        data = normal.json()
    except:
        print('Error. Retrying...')
        time.sleep(1)
        normal = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00026796&datatype=TMIN&datatype=TMAX&startdate='+date+'&enddate='+date+'&units=standard', headers={"token":"iaJCZkVywooFpyNRwIIsGuMcoMlzAWIa"})
        try:
            data = normal.json()
        except:
            print('An unknown error occurred. Your API key may have been limited. Try again later.')
            exit()
    high.append(data['results'][3]['value'])
    low.append(data['results'][4]['value'])
    time.sleep(0.5)
    print(str(day)+'/30 done!')
    day +=1

fig, ax = plot.subplots()
# Graph settings--------------------------------------
ax.plot(range(1, 31), low, linewidth=3, color='blue')
ax.plot(range(1, 31), high, linewidth=3, color='red')
ax.set_title((f"High's and Lows {date}"), fontsize=24)
ax.set_xlabel("Day", fontsize=14)
ax.set_ylabel("Temperature", fontsize=14)
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
# ----------------------------------------------------
plot.savefig(".other/output.jpg")
print('Saved chart to .other/output.jpg')
plot.show()