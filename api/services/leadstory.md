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

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/category?slug=technology&regions=0&limit=10&key=your_api_key"
```

### GET /categories

Retrieve articles from multiple categories at once. This endpoint allows you to fetch content from several categories in a single request.

**Parameters:**

- `ids` (required) - Comma-separated list of category IDs (e.g., "1,2,3")
- `regions` (required) - Region code
- `limit` (optional) - Number of articles to return

**Example Request:**

```bash
curl "https://www.vuepilot.com/api/v1/services/leadstory/categories?ids=1,2,3&regions=0&limit=10&key=your_api_key"
```

**Example Response:**

```json
[
  {
    "id": 123456,
    "slug": "major-tech-announcement",
    "title": "Major Tech Company Announces Revolutionary Product",
    "description": "Company XYZ revealed their latest innovation that could change the industry.",
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

**Available Categories:**

Categories are organized hierarchically. **Parent categories** (shown below) will include articles from all their child categories in the response, while **child categories** return only articles specific to that subcategory.

**Parent Categories:**

- `business` - Business (ID: 8) - includes all business-related subcategories
- `crime` - Crime (ID: 3) - includes all crime-related subcategories
- `entertainment` - Entertainment (ID: 10) - includes all entertainment subcategories
- `finance` - Finance (ID: 7) - includes all finance-related subcategories
- `health` - Health (ID: 5) - includes all health-related subcategories
- `lifestyle` - Lifestyle (ID: 4) - includes all lifestyle subcategories
- `politics` - Politics (ID: 2) - includes all political subcategories
- `social-issues` - Social Issues (ID: 220) - includes all social issue subcategories
- `sports` - Sports (ID: 9) - includes all sports subcategories
- `technology` - Technology (ID: 6) - includes all technology subcategories
- `world-news` - World News (ID: 1) - includes all international news

**Business Subcategories:**

- `companies-and-startups` - Companies & Startups (ID: 63)
- `economy` - Economy (ID: 66)
- `employment` - Employment (ID: 102)
- `energy` - Energy (ID: 120)
- `mining-and-resources` - Mining & Resources (ID: 186)
- `philanthropy` - Philanthropy (ID: 121)
- `retail` - Retail (ID: 65)
- `rural` - Rural & Agriculture (ID: 89)
- `transport` - Transport (ID: 13)

**Crime Subcategories:**

- `court` - Court (ID: 25)
- `cyber-crime` - Cyber Crime (ID: 27)
- `police` - Police (ID: 24)
- `protests` - Protests (ID: 26)
- `terrorism` - Terrorism (ID: 94)

**Entertainment Subcategories:**

- `art` - Art & Theatre (ID: 86)
- `celebrity` - Celebrity (ID: 81)
- `good-news` - Good News (ID: 16)
- `movies` - Movies (ID: 84)
- `music` - Music (ID: 85)
- `royal-family` - Royal Family (ID: 82)
- `tv` - TV (ID: 83)

**Finance Subcategories:**

- `banking-and-loans` - Banking & Loans (ID: 61)
- `crypto` - Crypto (ID: 60)
- `property` - Property & Architecture (ID: 58)
- `stockmarket` - Stockmarket (ID: 57)

**Health Subcategories:**

- `aged-care` - Aged Care (ID: 155)
- `cancer` - Cancer (ID: 44)
- `covid-19` - COVID-19 (ID: 45)
- `disability` - Disability (ID: 46)
- `fitness` - Fitness & Exercise (ID: 40)
- `food-and-diet` - Food & Diet (ID: 38)
- `heart-disease` - Heart Disease (ID: 42)
- `kids-health` - Kids Health (ID: 48)
- `medical-research` - Medical Research (ID: 39)
- `mental-health` - Mental Health (ID: 47)
- `pregnancy` - Pregnancy (ID: 41)

**Lifestyle Subcategories:**

- `Beauty` - Beauty (ID: 30)
- `cars` - Cars & Motoring (ID: 28)
- `education` - Education (ID: 34)
- `family` - Family & Parenting (ID: 33)
- `fashion` - Fashion (ID: 32)
- `media-journalism` - Media & Advertising (ID: 90)
- `pets-and-animals` - Pets & Animals (ID: 31)
- `shopping` - Shopping (ID: 36)
- `social-media` - Social Media (ID: 37)
- `travel` - Travel (ID: 29)

**Politics Subcategories:**

- `council-politics` - Council Politics (ID: 23)
- `greens` - Socialist Politics (ID: 20)
- `international-politics` - International Politics (ID: 22)
- `labor` - Left-Wing Politics (ID: 18)
- `liberal` - Right-Wing Politics (ID: 19)
- `minor-parties` - Minor Parties (ID: 21)

**Social Issues Subcategories:**

- `climate` - Climate (ID: 91)
- `environment` - Environment (ID: 222)
- `immigration` - Immigration (ID: 157)
- `lgbt` - LGBTQIA (ID: 15)
- `race-ethnicity` - Race & Ethnicity (ID: 99)
- `religion` - Religion (ID: 95)
- `womens-rights` - Women's Rights (ID: 17)

**Sports Subcategories:**

- `afl` - AFL (ID: 68)
- `athletics` - Athletics (ID: 80)
- `basketball` - Basketball (ID: 74)
- `boxing` - Boxing (ID: 252)
- `cricket` - Cricket (ID: 69)
- `cycling` - Cycling (ID: 87)
- `extreme-sports` - Extreme Sports (ID: 156)
- `football` - Football (ID: 70)
- `golf` - Golf (ID: 76)
- `horse-racing` - Horse Racing (ID: 77)
- `motorracing` - Motor Racing (ID: 71)
- `netball` - Netball (ID: 153)
- `nrl` - NRL (ID: 67)
- `olympics` - Olympics (ID: 73)
- `rugby-union` - Rugby Union (ID: 75)
- `swimming` - Swimming (ID: 79)
- `tennis` - Tennis (ID: 78)
- `womens-sports` - Women's Sports (ID: 72)

**Technology Subcategories:**

- `ai` - Artificial Intelligence (ID: 187)
- `android` - Samsung & Android (ID: 50)
- `apple` - Apple (ID: 49)
- `engineering` - Engineering & Construction (ID: 52)
- `gadgets` - Gadgets & Robotics (ID: 53)
- `pc` - PC (ID: 55)
- `science` - Science (ID: 51)
- `space` - Space Exploration (ID: 56)
- `sponsoredcontent` - Sponsored Content (ID: 219)
- `video-games` - Video Games (ID: 54)

**World News Subcategories:**

- `aviation` - Aviation (ID: 62)
- `disaster` - Disaster (ID: 221)
- `foreign-affairs` - Foreign Affairs (ID: 92)
- `history` - History (ID: 93)
- `humanrights` - Human Rights (ID: 100)
- `military-conflict` - Military & Conflict (ID: 12)
- `weather` - Weather (ID: 11)

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
