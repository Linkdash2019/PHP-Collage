from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plot
import requests
from pathlib import Path
import csv
import time
import os

search_list = []
date2 = []
high = []
low = []

path_csv = Path('multiTimeline.csv')
path_noaa_hot = Path('noaa_hot.txt')
path_noaa_cold = Path('noaa_cold.txt')
path_search_list = Path('search_list.txt')


year = 2024
month = 1
end = 31
display = ('')

myear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
myear_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

delay = 0.3

#Define the running directory
current_dir = os.path.dirname(os.path.abspath(__file__))

class MyClass:
    def __init__(self, s_year, s_month, s_end):
        self.year = s_year
        self.month = s_month
        self.end = s_end
        self.day = 1
    def download_google(self):
        input('This program will now open Chrome and download the required Google Trends data.\nPlease DO NOT do anything on the Chrome window!\nPress ENTER to start')
        if os.path.exists(current_dir + '/multiTimeline.csv'):
            os.remove(current_dir + '/multiTimeline.csv')
        else:
            pass
        global search_list, date2, high, low
        search_list = []
        date2 = []
        high = []
        low = []


        # Set window launch size and Download directory
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1024,768")
        chrome_options.add_experimental_option('prefs', {'download.default_directory': fr'{current_dir}'})
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        actions = ActionChains(driver)

        # Open the webpage
        driver.get('https://trends.google.com/trends/')

        # Search weather in Google Trends
        driver.find_element(By.XPATH,'/html/body/c-wiz/div/div[2]/div[4]/div[1]/c-wiz[1]/div/div[1]/div[3]/div/div/div[2]/div/div').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div/div/c-wiz/div/div/div/div/div[1]/div[2]/div/div').click()
        actions.send_keys("Weather").perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2+delay)

        # Change search region to Arizona
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/header/div/div[3]/ng-transclude/div[2]/div/div/hierarchy-picker[1]').click()
        time.sleep(0.5)
        actions.send_keys("Arizona").perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2+delay)

        # Change time search
        driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/header/div/div[3]/ng-transclude/div[2]/div/div/custom-date-picker').click()
        for _ in range(9):
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/md-dialog/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/md-content/form/div[1]/md-datepicker/div[1]/input').click()
        time.sleep(0.5)
        for _ in range(10):
            actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(f'{self.month}/1/{self.year}').perform()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/md-dialog/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/md-content/form/div[2]/md-datepicker/div[1]/input').click()
        time.sleep(0.5)
        for _ in range(10):
            actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(f'{self.month}/{self.end}/{self.year}').perform()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/md-dialog/md-dialog-actions/button[2]').click()
        time.sleep(3+delay)

        # Attempt Download
        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
                break
            except:
                print('Failed to find download button\nReloading page to try again.')
                time.sleep(5)
                driver.refresh()
                time.sleep(3+delay)

        time.sleep(2)

        # Close the browser
        driver.quit()
        print('Done downloading Google Trends data')

        # Remove first 2 lines from downloaded file
        for _ in range(2):
            with open(path_csv, 'rt') as fr:
                # reading line by line
                lines = fr.readlines()
                # pointer for position
                ptr = 1
                # opening in writing mode
                with open(path_csv, 'wt') as fw:
                    for line in lines:
                        if ptr != 1:
                            fw.write(line)
                        ptr += 1
    def google_csv_decode(self):
        lines = path_csv.read_text().splitlines()
        reader = csv.reader(lines)
        header_row = next(reader)

        for row in reader:
            try:
                search_weather = row[1]

            except ValueError:
                print(f"Missing data!")
                raise
            else:
                search_list.append(int(search_weather))

        with path_search_list.open(mode='w') as file:
            for item in high:
                file.write(f"{int(item)}\n")
    def download_noaa(self):
        input('This program will now download weather data from NOAA. \nPress ENTER to start')
        global display
        display = (self.month + '-' + self.year)
        print('Working... Please wait')
        while self.day <= self.end:
            date = (self.year + '-' + f"{int(self.month):02d}" + '-' + f"{self.day:02d}")
            normal = requests.get(
                'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00026796&datatype=TMIN&datatype=TMAX&startdate=' + date + '&enddate=' + date + '&units=standard', headers={"token": "iaJCZkVywooFpyNRwIIsGuMcoMlzAWIa"})
            try:
                data = normal.json()
            except:
                print('Error. Retrying...')
                time.sleep(1)
                normal = requests.get(
                    'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00026796&datatype=TMIN&datatype=TMAX&startdate=' + date + '&enddate=' + date + '&units=standard', headers={"token": "iaJCZkVywooFpyNRwIIsGuMcoMlzAWIa"})
                try:
                    data = normal.json()
                except:
                    print('An unknown error occurred. Skipping...')
            try:
                high.append(data['results'][3]['value'])
                low.append(data['results'][4]['value'])
            except:
                print('Missing data! Using last known data!')
                data = databak
                high.append(data['results'][3]['value'])
                low.append(data['results'][4]['value'])
            databak = data
            time.sleep(0.5)
            print(f'{self.day}/{self.end} done!')
            self.day += 1
        with path_noaa_hot.open(mode='w') as file:
            for item in high:
                file.write(f"{int(item)}\n")

        with path_noaa_cold.open(mode='w') as file:
            for item in low:
                file.write(f"{int(item)}\n")

        print('Finished downloading data.')
    def graph_display(self):
        #Read noaa data
        with path_noaa_hot.open(mode='r') as file:
            high = [int(line.strip()) for line in file]
        with path_noaa_cold.open(mode='r') as file:
            low = [int(line.strip()) for line in file]
        with path_search_list.open(mode='r') as file:
            search_list = [int(line.strip()) for line in file]
        self.end = 0
        for item in high:
            self.end+=1

        fig, (ax1, ax2) = plot.subplots(1, 2, layout='constrained')
        # Graph settings ax1-----------------------------------
        ax1.plot(range(1, self.end+1), low, linewidth=3, color='blue')
        ax1.plot(range(1, self.end+1), high, linewidth=3, color='red')
        ax1.set_title(f"High's and Lows\n{display}", fontsize=24)
        ax1.set_xlabel("Day", fontsize=14)
        ax1.set_ylabel("Temperature", fontsize=14)
        ax1.tick_params(labelsize=14)
        ax1.ticklabel_format(style='plain')
        # Graph settings ax2-----------------------------------
        ax2.bar(range(1, self.end+1), search_list, edgecolor="black", linewidth=0.7)
        ax2.set_title(f"Google search\npopularity", fontsize=24)
        ax2.set_xlabel("Day", fontsize=14)
        ax2.set_ylabel("Popularity\nPercentage", fontsize=14)
        ax2.tick_params(labelsize=14)
        # Other settings----------------------------------------
        mng = plot.get_current_fig_manager()
        mng.set_window_title('Final_Project.py Graph')
        mng.resize(1500,660)
        #-------------------------------------------------------
        plot.show()
    def get_date(self):
        # Set Month and Year to grab
        self.year = (input('Enter a year >>> '))
        self.month = (input('Enter a month >>> '))
        year = self.year
        month = self.month

        # Try for valid and Leap Year
        try:
            intyear = int(self.year)
            if intyear % 4 == 0:
                end = int(self.month)
                end = (myear_leap[end - 1])
            else:
                end = int(self.month)
                end = (myear[end - 1])
        except:
            print('Invalid response detected')
            print(f'Year: {self.year}\nMonth: {self.month}')
            print('Year should be a 4 digit number. e.g. 2022, 2004\nMonth should be a number from 1-12. e.g. 3, 10')
            exit()

        class1 = MyClass(self.year, self.month, end)
        try:
            class1.download_google()
        except:
            print('The program could not finish downloading the Google Trends data correctly.\nThis is often a result of a less speedy internet connection.\nUse option 3 in the menu to set a delay.')
            return
        print()
        class1.download_noaa()
        print()
        return end


if not path_csv.is_file():
    input('Hello, it appears to be your first time here.\nLets get you set up!\nPress [ENTER] to continue')
    input('\n\nYou will need to input a month and year you would like to pull data from.\nIt must be formated like so\nMonth - Any number from 1-12\nYear - A four digit number starting at 2004\nPress [ENTER] to proceed')
    class2 = MyClass(year, month, end)
    end = class2.get_date()
    class2.google_csv_decode()

print('Options:\n1 - Display graph\n2 - Change Month and Year to download\n3 - Change Chrome download delay\n4 - Exit')
while True:
    try:
        user_input = int(input('What would you like to do? >>> '))
    except:
        user_input = 0

    if user_input == 1:
        class2 = MyClass(year, month, end)
        try:
            class2.graph_display()
        except:
            print('Error: Graph data may be corrupted or download Month and Year was not set!\nPlease choose option 2 in the main menu')
    elif user_input == 2:
        class2 = MyClass(year, month, end)
        end = class2.get_date()
        class2.google_csv_decode()
    elif user_input == 3:
        print('If Chrome is struggling to download the Google Trends data adding a delay may help.')
        delay = int(input('What would you like the Chrome delay to be (in seconds) \nThis is temperamental\n>>> '))
    elif user_input == 4:
        exit()
    else:
        print('Options:\n1 - Display graph\n2 - Change Month and Year to download\n3 - Change Chrome download delay\n4 - Exit')
