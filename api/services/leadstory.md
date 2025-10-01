# LeadStory Service

## Description

Access global breaking news, trending and category specific content from publishers around from around the world direct from LeadStory.

## Base Path

```
/api/v1/services/leadstory
```

## Authentication

Include your API key as a URL parameter: `?key=your_api_key_here`

See [usage documentation](README.md) for detailed authentication information.

## Regions

Regions are used to filter content by country or geographical area. When making API requests to services that support regional filtering (such as the LeadStory service), you can specify one or more region IDs to customize the content returned.

Multiple regions can be combined using comma-separated values (e.g., `regions=1,2,0` for Australia, United States, and Global).

**Note** The majority of publishers on LeadStory are global publishers (region=0) so you will need to include `0` in the regions list to get the most results.

### Available Regions

| ID  | Name           | Code |
| --- | -------------- | ---- |
| 0   | Global         | GL   |
| 1   | Australia      | AU   |
| 2   | United States  | US   |
| 3   | United Kingdom | UK   |
| 4   | Europe         | EU   |
| 5   | Canada         | CA   |
| 6   | Singapore      | SG   |
| 7   | Israel         | IL   |
| 8   | New Zealand    | NZ   |

**Example:** To get content for United States and Canada: `?regions=2,5&key=your_api_key`

## Endpoints

### GET /breaking

Retrieve breaking news articles by region.

**Parameters:**

- `regions` (required) - Region code (e.g., "0" for global)
- `limit` (optional) - Number of articles to return (default: 15)

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/breaking?regions=0&limit=10&key=your_api_key"
```

**Example Response:**

```json
[
	{
		"id": 123456,
		"slug": "major-tech-announcement",
		"title": "Major Tech Company Announces Revolutionary Product",
		"description": "Company XYZ revealed their latest innovation that could change the industry. The new product has made waves across the entire industry",
		"created_at": "2025-01-15T14:30:00Z",
		"publisher": {
			"name": "Tech News Daily",
			"icon_url": "https://assets.leadstory.com/publishers/123/images/icon.jpg"
		},
		"media": [
			{
				"assets": [
					{
						"file_type": "jpg",
						"height": 1080,
						"width": 1920,
						"url": "https://cdn.jwplayer.com/v2/media/abc123/poster.jpg?width=1920"
					},
					{
						"file_type": "jpg",
						"height": 720,
						"width": 1280,
						"url": "https://cdn.jwplayer.com/v2/media/abc123/poster.jpg?width=1280"
					}
				]
			}
		],
		"categories": [
			{
				"slug": "technology",
				"title": "Technology"
			}
		]
	}
]
```

### GET /pulse

Retrieve pulse articles. Pulse or "need to know" is a feed of the highest relevance articles across a broad range of categories which provides a blend of breaking and interesting articles.

**Parameters:**

- `regions` (required) - Region code
- `limit` (optional) - Number of articles to return

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/pulse?regions=0&limit=5&key=your_api_key"
```

### GET /trending

Retrieve trending articles by region.

**Parameters:**

- `regions` (required) - Region code
- `limit` (optional) - Number of articles to return

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/trending?regions=0&limit=8&key=your_api_key"
```

### GET /category

Retrieve articles from a specific category.

**Parameters:**

- `slug` (required) - Category slug (see available categories below)
- `regions` (required) - Region code
- `limit` (optional) - Number of articles to return

**Available Category Slugs:**

Categories are organized hierarchically. **Parent categories** (shown below) will include articles from all their child categories in the response, while **child categories** return only articles specific to that subcategory.

**Parent Categories:**

- `business` - Business (includes all business-related subcategories)
- `crime` - Crime (includes all crime-related subcategories)
- `entertainment` - Entertainment (includes all entertainment subcategories)
- `finance` - Finance (includes all finance-related subcategories)
- `health` - Health (includes all health-related subcategories)
- `lifestyle` - Lifestyle (includes all lifestyle subcategories)
- `politics` - Politics (includes all political subcategories)
- `social-issues` - Social Issues (includes all social issue subcategories)
- `sports` - Sports (includes all sports subcategories)
- `technology` - Technology (includes all technology subcategories)
- `world-news` - World News (includes all international news)

**Business Subcategories:**

- `companies-and-startups` - Companies & Startups
- `economy` - Economy
- `employment` - Employment
- `energy` - Energy
- `mining-and-resources` - Mining & Resources
- `philanthropy` - Philanthropy
- `retail` - Retail
- `rural` - Rural & Agriculture
- `transport` - Transport

**Crime Subcategories:**

- `court` - Court
- `cyber-crime` - Cyber Crime
- `police` - Police
- `protests` - Protests
- `terrorism` - Terrorism

**Entertainment Subcategories:**

- `art` - Art & Theatre
- `celebrity` - Celebrity
- `good-news` - Good News
- `movies` - Movies
- `music` - Music
- `royal-family` - Royal Family
- `tv` - TV

**Finance Subcategories:**

- `banking-and-loans` - Banking & Loans
- `crypto` - Crypto
- `property` - Property & Architecture
- `stockmarket` - Stockmarket

**Health Subcategories:**

- `aged-care` - Aged Care
- `cancer` - Cancer
- `covid-19` - COVID-19
- `disability` - Disability
- `fitness` - Fitness & Exercise
- `food-and-diet` - Food & Diet
- `heart-disease` - Heart Disease
- `kids-health` - Kids Health
- `medical-research` - Medical Research
- `mental-health` - Mental Health
- `pregnancy` - Pregnancy

**Lifestyle Subcategories:**

- `beauty` - Beauty
- `cars` - Cars & Motoring
- `education` - Education
- `family` - Family & Parenting
- `fashion` - Fashion
- `media-journalism` - Media & Advertising
- `pets-and-animals` - Pets & Animals
- `shopping` - Shopping
- `social-media` - Social Media
- `travel` - Travel

**Politics Subcategories:**

- `council-politics` - Council Politics
- `greens` - Socialist Politics
- `international-politics` - International Politics
- `labor` - Left-Wing Politics
- `liberal` - Right-Wing Politics
- `minor-parties` - Minor Parties

**Social Issues Subcategories:**

- `climate` - Climate
- `environment` - Environment
- `immigration` - Immigration
- `lgbt` - LGBTQIA
- `race-ethnicity` - Race & Ethnicity
- `religion` - Religion
- `womens-rights` - Women's Rights

**Sports Subcategories:**

- `afl` - AFL
- `athletics` - Athletics
- `basketball` - Basketball
- `boxing` - Boxing
- `cricket` - Cricket
- `cycling` - Cycling
- `extreme-sports` - Extreme Sports
- `football` - Football
- `golf` - Golf
- `horse-racing` - Horse Racing
- `motorracing` - Motor Racing
- `netball` - Netball
- `nrl` - NRL
- `olympics` - Olympics
- `rugby-union` - Rugby Union
- `swimming` - Swimming
- `tennis` - Tennis
- `womens-sports` - Women's Sports

**Technology Subcategories:**

- `ai` - Artificial Intelligence
- `android` - Samsung & Android
- `apple` - Apple
- `engineering` - Engineering & Construction
- `gadgets` - Gadgets & Robotics
- `pc` - PC
- `science` - Science
- `space` - Space Exploration
- `sponsoredcontent` - Sponsored Content
- `video-games` - Video Games

**World News Subcategories:**

- `aviation` - Aviation
- `disaster` - Disaster
- `foreign-affairs` - Foreign Affairs
- `history` - History
- `humanrights` - Human Rights
- `military-conflict` - Military & Conflict
- `weather` - Weather

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/category?slug=technology&regions=0&limit=10&key=your_api_key"
```

## Usage Examples

### JavaScript

```javascript
// Get breaking news
const response = await fetch(
	"https://www.vuepilot.com/api/v1/services/leadstory/breaking?regions=0&limit=10&key=your_api_key"
);
const news = await response.json();

// Get technology articles
const techResponse = await fetch(
	"https://www.vuepilot.com/api/v1/services/leadstory/category?slug=technology&regions=0&limit=5&key=your_api_key"
);
const techNews = await techResponse.json();
```

### Python

```python
import requests

# Get breaking news
response = requests.get(
    'https://www.vuepilot.com/api/v1/services/leadstory/breaking',
    params={'regions': '0', 'limit': 10, 'key': 'your_api_key'}
)
news = response.json()
```
