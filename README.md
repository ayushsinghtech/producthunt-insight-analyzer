# Product Hunt Insight Scraper

## Overview

The **Product Hunt Insight Scraper** is a Python-based tool that extracts trending product data from Product Hunt's GraphQL API. It fetches key insights including:

- Product names
- Taglines (launch copy)
- Tags and categories
- Engagement metrics (votes, comments)

This tool helps analyze what kind of products perform well and resonate on Product Hunt — useful for marketing, product research, and competitive analysis.

---

## Features

-  Fetches top trending products by upvotes
-  Retrieves taglines, tags, upvotes, and comment counts
-  Uses GraphQL API for efficient data querying
-  Outputs results in readable JSON format
-  Saves output locally to `output.json`
-  Secure API token handling via `.env`

---

##  Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/producthunt-insight-analyzer.git
cd producthunt-insight-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
Make sure Python 3.7+ is installed.
```
### 3. Set Up Environment Variable

Create a .env file in the root directory with this content:
PRODUCTHUNT_API_TOKEN=your_access_token_here

### 4. Run the Scraper

```bash
python producthunt_scraper.py
```
This will:
Print the scraped data in the console

Save the results to output.json

### Sample Output Format
json
{
  "name": "Startup Stash",
  "tagline": "A curated directory of 400 resources & tools for startups",
  "votes": 9321,
  "comments": 321,
  "tags": ["Web App", "Tech", "Startup Lessons"]
}

### Notes
API Token: Get yours from Product Hunt Developer Portal
Rate Limiting: Be cautious of API rate limits when making multiple requests.

### License
MIT License

### Acknowledgements
Thanks to Product Hunt for the API access and inspiration.