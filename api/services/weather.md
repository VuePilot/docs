# Weather Service

## Description

Get weather forecast data for any location using latitude and longitude coordinates.

## Base Path

```
/api/v1/services/weather
```

## Authentication

Include your API key as a URL parameter: `?key=your_api_key_here`

See [usage documentation](README.md) for detailed authentication information.

## Endpoints

### GET /forecast

Retrieve weather forecast for specified coordinates.

**Parameters:**

- `lat` (required) - Latitude coordinate
- `lon` (required) - Longitude coordinate
- `unit` (required) - Unit system: "metric" or "imperial"

**Example Request:**

```bash
# New York City weather in metric units
curl "https://www.vuepilot.com/api/v1/services/weather/forecast?lat=40.7128&lon=-74.0060&unit=metric&key=your_api_key"

# Imperial units example
curl "https://www.vuepilot.com/api/v1/services/weather/forecast?lat=40.7128&lon=-74.0060&unit=imperial&key=your_api_key"
```

**Example Response:**

```json
{
	"lat": 40.7128,
	"lon": -74.006,
	"timezone": "America/New_York",
	"timezone_offset": -14400,
	"current": {
		"temp": 16.9,
		"feels_like": 16.79,
		"sunrise": 1759229497,
		"sunset": 1759272006,
		"result": {
			"main": "Clouds",
			"description": "overcast clouds",
			"icon_url": "https://assets.vuepilot.com/images/icons/weather/clouds.webp"
		}
	},
	"daily": [
		{
			"dt": 1759248000,
			"summary": "There will be partly cloudy today",
			"temp": {
				"day": 24.26,
				"max": 25.83,
				"min": 16.9
			},
			"feels_like": {
				"day": 23.66,
				"night": 20.73
			},
			"result": {
				"main": "Clouds",
				"description": "overcast clouds",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sun-clouds.webp"
			}
		},
		{
			"dt": 1759334400,
			"summary": "You can expect partly cloudy in the morning, with clearing in the afternoon",
			"temp": {
				"day": 18.36,
				"max": 20.9,
				"min": 14.13
			},
			"feels_like": {
				"day": 17.11,
				"night": 14.92
			},
			"result": {
				"main": "Clouds",
				"description": "scattered clouds",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sun-clouds.webp"
			}
		},
		{
			"dt": 1759420800,
			"summary": "The day will start with clear sky through the late morning hours, transitioning to partly cloudy",
			"temp": {
				"day": 16.27,
				"max": 18.23,
				"min": 12.54
			},
			"feels_like": {
				"day": 14.94,
				"night": 14.96
			},
			"result": {
				"main": "Clouds",
				"description": "broken clouds",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sun-clouds.webp"
			}
		},
		{
			"dt": 1759507200,
			"summary": "You can expect partly cloudy in the morning, with clearing in the afternoon",
			"temp": {
				"day": 17.73,
				"max": 21.87,
				"min": 14.19
			},
			"feels_like": {
				"day": 16.73,
				"night": 17.75
			},
			"result": {
				"main": "Clouds",
				"description": "broken clouds",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sun-clouds.webp"
			}
		},
		{
			"dt": 1759593600,
			"summary": "You can expect clear sky in the morning, with partly cloudy in the afternoon",
			"temp": {
				"day": 21.39,
				"max": 26.9,
				"min": 15.99
			},
			"feels_like": {
				"day": 20.84,
				"night": 21.34
			},
			"result": {
				"main": "Clear",
				"description": "clear sky",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sunny.webp"
			}
		},
		{
			"dt": 1759680000,
			"summary": "There will be partly cloudy until morning, then clearing",
			"temp": {
				"day": 23.5,
				"max": 26.71,
				"min": 18.96
			},
			"feels_like": {
				"day": 23.08,
				"night": 21.14
			},
			"result": {
				"main": "Clear",
				"description": "clear sky",
				"icon_url": "https://assets.vuepilot.com/images/icons/weather/sunny.webp"
			}
		}
	]
}
```

**Units:**

- **Metric**: Temperature in Celsius, wind speed in m/s
- **Imperial**: Temperature in Fahrenheit, wind speed in mph

## Response Fields

### Current Weather

- `temp` - Current temperature
- `feels_like` - Perceived temperature
- `sunrise` - Sunrise time (Unix timestamp)
- `sunset` - Sunset time (Unix timestamp)
- `result.main` - Weather condition (Clear, Clouds, Rain, etc.)
- `result.description` - Detailed weather description
- `result.icon_url` - Weather icon URL

### Daily Forecast

- `dt` - Date (Unix timestamp)
- `summary` - Daily weather summary
- `temp.day` - Day temperature
- `temp.max` - Maximum temperature
- `temp.min` - Minimum temperature
- `feels_like.day` - Perceived day temperature
- `feels_like.night` - Perceived night temperature

## Usage Examples

### JavaScript

```javascript
// Get current weather
const response = await fetch(
	"https://www.vuepilot.com/api/v1/services/weather/forecast?lat=40.7128&lon=-74.0060&unit=metric&key=your_api_key"
);
const weather = await response.json();

console.log(`Current temperature: ${weather.current.temp}°C`);
console.log(`Condition: ${weather.current.result.description}`);
```

### Python

```python
import requests

# Get weather forecast
response = requests.get(
    'https://www.vuepilot.com/api/v1/services/weather/forecast',
    params={
        'lat': 40.7128,
        'lon': -74.0060,
        'unit': 'metric',
        'key': 'your_api_key'
    }
)
weather = response.json()

print(f"Current temperature: {weather['current']['temp']}°C")
print(f"7-day forecast available with {len(weather['daily'])} days")
```

## Getting Coordinates

Use the [Location Service](location.md) to automatically detect coordinates based on IP address, or use any geocoding service to convert addresses to latitude/longitude coordinates.
