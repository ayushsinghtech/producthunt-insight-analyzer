from dotenv import load_dotenv
load_dotenv()
import requests
import json
import os
import sys

# Load API token from environment variable
API_URL = "https://api.producthunt.com/v2/api/graphql"
TOKEN = os.getenv("PRODUCTHUNT_API_TOKEN")

if not TOKEN:
    print("Error: Set environment variable PRODUCTHUNT_API_TOKEN with your Product Hunt API token.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

query = """
{
  posts(order: VOTES) {
    edges {
      node {
        name
        tagline
        votesCount
        commentsCount
        topics {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

def fetch_trending_products():
    response = requests.post(API_URL, headers=HEADERS, json={"query": query})
    if response.status_code == 200:
        data = response.json()
        results = []
        for edge in data["data"]["posts"]["edges"]:
            product = edge["node"]
            results.append({
                "name": product["name"],
                "tagline": product["tagline"],
                "votes": product["votesCount"],
                "comments": product["commentsCount"],
                "tags": [t["node"]["name"] for t in product["topics"]["edges"]]
            })
        return results
    else:
        raise Exception(f"GraphQL query failed with status code {response.status_code}: {response.text}")

def save_to_file(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Output saved to {filename}")

if __name__ == "__main__":
    try:
        trending_products = fetch_trending_products()
        print(json.dumps(trending_products, indent=2, ensure_ascii=False))
        save_to_file(trending_products)
    except Exception as e:
        print(f"Error: {e}")
