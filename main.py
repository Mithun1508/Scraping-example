import time
import requests
from bs4 import BeautifulSoup

city = "INXX0096:1:IN"  # Delhi city code
city_name = "Delhi"

def get_temp_tag(tag):
    return tag.has_attr('class') and any(
        "CurrentConditions--tempValue--" in str(i) for i in tag['class'])

def fetch_weather(city):
    url = f"https://weather.com/weather/today/l/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find(get_temp_tag)
    temperature = element.text if element else "not available"
    return temperature

print(
    "Weather script is running."
    f" Will keep checking the current weather in {city_name} every 30 seconds...\n\n"
)

if __name__ == "__main__":
    while True:
        current_temperature = fetch_weather(city)
        print(f"Current temperature in {city_name}: {current_temperature}")
        time.sleep(30)
