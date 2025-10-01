# Location Service

## Description

Detect geographical location information based on IP address.
Can be used to detect your local city's longitude and latitude for use with the weather API.

## Base Path

```
/api/v1/services/location
```

## Authentication

Include your API key as a URL parameter: `?key=your_api_key_here`

See [usage documentation](README.md) for detailed authentication information.

## Endpoints

### GET /detect

Automatically detect location based on the requesting IP address.

**Parameters:**
None required - uses automatic IP detection.

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/location/detect?key=your_api_key"
```

**Example Response:**

```json
{
	"country": "United States",
	"country_code": "US",
	"region": "New York",
	"region_code": "NY",
	"city": "New York",
	"zip": "10001",
	"lat": 40.7128,
	"lon": -74.006,
	"timezone": "America/New_York",
	"isp": "Example ISP",
	"org": "Example Organization"
}
```

## Response Fields

- `country` - Full country name
- `country_code` - ISO country code (2 letters)
- `region` - State/province name
- `region_code` - State/province code
- `city` - City name
- `zip` - Postal/ZIP code
- `lat` - Latitude coordinate
- `lon` - Longitude coordinate
- `timezone` - IANA timezone identifier
- `isp` - Internet Service Provider name
- `org` - Organization name

## Usage Examples

### JavaScript

```javascript
// Detect current location
const response = await fetch("/api/v1/services/location/detect?key=your_api_key");
const location = await response.json();

console.log(`Location: ${location.city}, ${location.region}, ${location.country}`);
console.log(`Coordinates: ${location.lat}, ${location.lon}`);

// Use coordinates with weather service
const weatherResponse = await fetch(
	`/api/v1/services/weather/forecast?lat=${location.lat}&lon=${location.lon}&unit=metric&key=your_api_key`
);
const weather = await weatherResponse.json();
```

### Python

```python
import requests

# Detect location
location_response = requests.get(
    'https://www.vuepilot.com/api/v1/services/location/detect',
    params={'key': 'your_api_key'}
)
location = location_response.json()

print(f"Detected location: {location['city']}, {location['region']}")
print(f"Coordinates: {location['lat']}, {location['lon']}")

# Use with weather service
weather_response = requests.get(
    'https://www.vuepilot.com/api/v1/services/weather/forecast',
    params={
        'lat': location['lat'],
        'lon': location['lon'],
        'unit': 'metric',
        'key': 'your_api_key'
    }
)
weather = weather_response.json()
```

## Integration with Weather Service

The location service is particularly useful when combined with the [Weather Service](weather.md). Use the detected `lat` and `lon` coordinates to automatically get weather data for the user's current location:

```javascript
// Auto-detect location and get local weather
async function getLocalWeather() {
	// Get location
	const locationResponse = await fetch("https://www.vuepilot.com/api/v1/services/location/detect?key=your_api_key");
	const location = await locationResponse.json();

	// Get weather for detected location
	const weatherResponse = await fetch(
		`https://www.vuepilot.com/api/v1/services/weather/forecast?lat=${location.lat}&lon=${location.lon}&unit=metric&key=your_api_key`
	);
	const weather = await weatherResponse.json();

	return {
		location: `${location.city}, ${location.region}`,
		weather: weather.current,
	};
}
```

## Privacy Notes

- Location detection is based on IP address geolocation
- Accuracy varies by location and ISP
- Results are cached to improve performance
- No personal data is stored or tracked
