import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API to get the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The number of subscribers for the subreddit (integer), or 0 if the subreddit is invalid.
  """

  # Base URL for the subreddit information endpoint
  base_url = "https://www.reddit.com/r/"

  # Construct the URL with the subreddit name
  url = f"{base_url}{subreddit}/about.json"

  # Make the GET request, disallowing redirects
  response = requests.get(url, allow_redirects=False)

  # Check if request was successful (200 OK)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    # Access the subscriber count from the data (adjust based on Reddit API structure)
    return data.get("data", {}).get("subscribers", 0)
  else:
    # Invalid subreddit, return 0
    return 0

# Example usage
subreddit_name = "learnpython"
subscribers = number_of_subscribers(subreddit_name)

if subscribers > 0:
  print(f"The subreddit r/{subreddit_name} has {subscribers} subscribers.")
else:
  print(f"The subreddit r/{subreddit_name} is invalid or not found.")

