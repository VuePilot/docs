# VuePilot Services API

The VuePilot Services API provides access to external data services for digital signage applications.

**The Services API is an enterprise feature** that must be enabled for your account. If you attempt to access these endpoints without the Services API enabled, you will receive a `401 Unauthorized` response

## Authentication

Include your API key as a URL parameter:

```
?key=your_api_key_here
```

API keys can be either:

- User API keys (starting with `U_`)
- License keys (for machine authentication)

You can retrieve your user API key from the `Profile` section on the dashboard (https://www.vuepilot.com/users/edit).

We recommend creating a service user account instead of your own personal user account when using user API keys for production services.

## Rate Limiting

Rate limit will apply based on your accounts licensing parameters

## Integration Examples

### JavaScript/Fetch

```javascript
// Get weather data
const response = await fetch(
  "/api/v1/services/weather/forecast?lat=40.7128&lon=-74.0060&unit=metric&key=your_api_key"
);
const weatherData = await response.json();

// Get news data
const newsResponse = await fetch(
  "/api/v1/services/leadstory/breaking?regions=0&limit=10&key=your_api_key"
);
const newsData = await newsResponse.json();
```

### cURL Examples

```bash
# Get breaking news
curl "https://www.vuepilot.com/api/v1/services/leadstory/breaking?regions=0&limit=5&key=your_api_key"

# Get weather forecast
curl "https://www.vuepilot.com/api/v1/services/weather/forecast?lat=37.7749&lon=-122.4194&unit=imperial&key=your_api_key"

# Detect location
curl "https://www.vuepilot.com/api/v1/services/location/detect?key=your_api_key"
```

### Python/Requests

```python
import requests

# Get weather data
weather_response = requests.get(
    'https://www.vuepilot.com/api/v1/services/weather/forecast',
    params={
        'lat': 40.7128,
        'lon': -74.0060,
        'unit': 'metric',
        'key': 'your_api_key_here'
    }
)
weather_data = weather_response.json()

# Get news data
news_response = requests.get(
    'https://www.vuepilot.com/api/v1/services/leadstory/breaking',
    params={
        'regions': '0',
        'limit': 10,
        'key': 'your_api_key_here'
    }
)
news_data = news_response.json()

# Get location data
location_response = requests.get(
    'https://www.vuepilot.com/api/v1/services/location/detect',
    params={
        'key': 'your_api_key_here'
    }
)
location_data = location_response.json()
```

## Available Services

- [LeadStory Service](leadstory.md) - Breaking news, trending articles, and category-specific content
- [Weather Service](weather.md) - Weather forecast data for any location
- [Location Service](location.md) - IP-based geographical location detection

## Support

For API support, please contact our development team or refer to the main VuePilot documentation.
