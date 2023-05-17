# Ditto Knowmad

Python Client for the Ditto API.


## Usage

You can interact with our API simply with the commands.

To get tweets about Lebron James:
```python
import os

from ditto-knowmad import DittoClient

client = DittoClient(api_key=os.getenv('<YOUR-API-KEY-HERE>'))
results = client.get_posts_from_source(query="lebron", sources=["tweets"])

print(results)
```

If you don't have an API key, email team@ditto.fyi to start working with us.

## Possible Sources (updated 5/17/23)

Below is an example list with all currently possible sources
```python
sources = [
  "tweets", # Twitter
  "tiktok_comments", # TikTok Comments
  "reddit_posts", # Reddit Posts
]
```

## License

This repo is under the [MIT License](https://opensource.org/license/mit/).