import requests
import json

# Constants
API_URL = "https://api.producthunt.com/v2/api/graphql"
HEADERS = {
    "Authorization": "Bearer PFakEv2pVdb_KH4p_9oY_WvwVBMQycHT0adukfWLuio",  # Replace with your token if needed
    "Content-Type": "application/json"
}

# GraphQL query to fetch top trending posts by votes (no date filter)
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
