
# Weather Scraping Project

## Overview

This project is a weather scraping tool that allows you to retrieve real-time weather data from various sources on the internet. It is designed to provide a simple and extensible solution for collecting weather information for different locations.

## Features

- **Real-Time Data:** Retrieve up-to-date weather information for specified locations.
  
- **Customizable:** Easily configure the tool to scrape data from different weather websites.
  
- **Data Formats:** Output weather data in various formats such as JSON, CSV, or plain text.

## Getting Started

### Prerequisites

- Python 3
  
- BeautifulSoup (for web scraping)
  
- Requests (for making HTTP requests)

### Installation


pip install beautifulsoup4 requests

git clone https://github.com/yourusername/weather-scraping.git

cd weather-scraping

Configure your target locations in the config.json file.
Run the scraper:

python weather_scraper.py

View the output in the specified format.

## Configuration
Edit the config.json file to customize the following parameters:

json
Copy code
{
  "locations": [
    {
      "name": "City1",
      "url": "https://weather-source.com/city1"
    },
    {
      "name": "City2",
      "url": "https://weather-source.com/city2"
    }
    // Add more locations as needed
  ],
  "output_format": "json"
}

![Weather script](https://github.com/Mithun1508/WeatherScraping/assets/93249038/70579ecc-5a65-43fe-928a-d314e8dcfc3d)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
