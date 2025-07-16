# Product Hunt Insight Scraper

## Overview

The **Product Hunt Insight Scraper** is a Python-based tool designed to extract valuable insights from Product Hunt's platform using their official GraphQL API. It gathers data on the top trending products, including product names, launch taglines, engagement metrics such as upvotes and comments, and associated tags/categories. This enables detailed analysis of what resonates in the digital product space.

---

## Features

- **Top Trending Products:** Retrieves the highest-voted products currently trending on Product Hunt.
- **Tags and Categories:** Extracts tags and categories associated with each product for thematic analysis.
- **Launch Copy & Taglines:** Captures product taglines which serve as launch copy summaries.
- **Engagement Metrics:** Collects quantitative engagement data including upvotes and comment counts.
- **JSON Output:** Outputs results in a structured JSON format for easy integration and further processing.
- **Save to File:** Automatically saves the fetched data to a local `output.json` file.

---

## Prerequisites

- Python 3.7 or higher
- A valid **Product Hunt API access token** with at least `public` scope.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd producthunt-insight-scraper

2. Install Dependencies
Use pip to install the required Python packages:

bash
pip install -r requirements.txt

3. Obtain Product Hunt API Access Token
Register an application on the Product Hunt Developer Portal.

Follow the OAuth2 authorization code flow to obtain an access token with the necessary scopes (public).

Replace the Authorization header's bearer token in producthunt_scraper.py with your token:

HEADERS = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE",
    "Content-Type": "application/json"
}
Usage
Run the scraper script from the command line:
bash
python producthunt_scraper.py
The script will print the fetched trending products data in JSON format to the console.

It will also save the output to output.json in the project directory.

Output Format:
Each product in the output JSON contains:

Field	Description
name	Name of the product
tagline	Launch copy/tagline of the product
votes	Number of upvotes
comments	Number of comments
tags	List of associated tags/categories

Example snippet:

json
{
  "name": "Startup Stash",
  "tagline": "A curated directory of 400 resources & tools for startups",
  "votes": 9321,
  "comments": 321,
  "tags": [
    "Web App",
    "Tech",
    "Startup Lessons"
  ]
}

Notes and Recommendations
Security: Never expose your API tokens publicly. For enhanced security, consider using environment variables or configuration files excluded from version control.

Rate Limits: Be mindful of Product Hunt API rate limits and plan requests accordingly.

Extensibility: Pagination and filtering features can be added to fetch more data or tailor the query to specific date ranges.

Error Handling: The script includes basic error handling; however, more robust exception management can be implemented.

License
This project is released under the MIT License.

Thank you for reviewing the Product Hunt Insight Scraper!
Happy coding and product hunting! 