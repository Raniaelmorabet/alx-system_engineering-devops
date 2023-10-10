#!/usr/bin/python3
""" raddit api"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0"}  # Set your user agent here

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts found.")
        return

    data = response.json()
    children = data.get("data", {}).get("children", [])

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

    after = data.get("data", {}).get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)
