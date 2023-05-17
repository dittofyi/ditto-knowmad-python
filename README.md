# Ditto Knowmad

Python Client for the Ditto API.

## Installation

You can install this package with:

```bash
pip install git+https://github.com/dittofyi/ditto-knowmad-python.git
```

We're not publishing it on PyPI yet. If you're working with us, we'll let you know
when it's time to update. You may need to `pip uninstall ditto_knowmad` before reinstalling
from here.

## Usage

You can interact with our API as shown below.

To get tweets about Lebron James:
```python
import os

from ditto_knowmad.DittoClient import DittoClient

client = DittoClient(api_key=os.getenv('<YOUR-API-KEY-HERE>'))
results = client.get_posts_from_source(query="lebron", sources=["tweets"])

print(results)
```

If you don't have an API key, email team@ditto.fyi to start working with us.

## Possible Sources (updated 5/17/23)

Below is an example list with all currently possible sources. Use any or all of these in your requests.
```python
sources = [
  "tweets", # Twitter
  "tiktok_comments", # TikTok comments
  "reddit_posts", # Reddit posts
]
```

## License

This repo is under the [MIT License](https://opensource.org/license/mit/).
