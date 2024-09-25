import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.weather.gov.hk/tc/wxinfo/pastwx/mws2024/mws202408.htm"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    soup = bs(content, "html.parser")

    weather_data = []
    weathers = soup.find_all("td")
    for weather in weathers:
        weather_value = weather.string
        if weather_value and weather_value.strip().isdigit():
            weather_data.append(float(weather_value.strip()))

    print(len(weather_data))
    print(weather_data[:50])

    if len(weather_data) >= 24:  
        x = np.arange(24)
        y = weather_data[:24]  
        fig, ax = plt.subplots()
        ax.plot(x, y) 
        plt.xlabel('Hour of the day')
        plt.ylabel('Weather Value')
        plt.title('Weather Data Over 24 Hours')
        plt.show()
    else:
        print("Not enough weather data available.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")