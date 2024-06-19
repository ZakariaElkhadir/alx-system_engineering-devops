# Reddit API Project

This project involves querying the Reddit API to extract specific information about subreddits. The tasks include getting the number of subscribers for a subreddit, printing the top ten hot posts, and recursively retrieving all hot articles for a subreddit.

## Tasks

### Task 0: How Many Subs?

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

#### Requirements
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- Do not follow redirects for invalid subreddits.
- Ensure you set a custom User-Agent to avoid `Too Many Requests` errors.

#### Testing
Create a script `0-main.py` to test the function. It should take a subreddit name as an argument and print the number of subscribers.

### Task 1: Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

#### Requirements
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print `None`.
- Do not follow redirects for invalid subreddits.

#### Testing
Create a script `1-main.py` to test the function. It should take a subreddit name as an argument and print the titles of the top ten hot posts.

### Task 2: Recurse It!

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return `None`.

#### Requirements
- Prototype: `def recurse(subreddit, hot_list=[])`
- The function must be able to be called with just a subreddit supplied.
- If not a valid subreddit, return `None`.
- Do not follow redirects for invalid subreddits.
- The function should use recursion, not loops.

#### Testing
Create a script `2-main.py` to test the function. It should take a subreddit name as an argument and print the number of hot articles found.

## Repository Structure

- **GitHub repository**: `alx-system_engineering-devops`
- **Directory**: `0x16-api_advanced`
- **Files**:
  - `0-subs.py`: Contains the function for Task 0.
  - `1-top_ten.py`: Contains the function for Task 1.
  - `2-recurse.py`: Contains the function for Task 2.

## Usage

1. Ensure you have the `requests` library installed.
2. Place the respective function in its corresponding file (`0-subs.py`, `1-top_ten.py`, `2-recurse.py`).
3. Use the provided test scripts (`0-main.py`, `1-main.py`, `2-main.py`) to test the functions.

## Examples

```bash
# Task 0: How Many Subs?
python3 0-main.py programming
# Expected output: Number of subscribers for 'programming' subreddit

python3 0-main.py this_is_a_fake_subreddit
# Expected output: 0

# Task 1: Top Ten
python3 1-main.py programming
# Expected output: Titles of the top 10 hot posts for 'programming' subreddit

python3 1-main.py this_is_a_fake_subreddit
# Expected output: None

# Task 2: Recurse It!
python3 2-main.py programming
# Expected output: Number of hot articles for 'programming' subreddit

python3 2-main.py this_is_a_fake_subreddit
# Expected output: None
```

Ensure that you adhere to the specified prototypes and requirements for each function to pass the checks successfully.
