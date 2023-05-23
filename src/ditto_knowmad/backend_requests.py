import aiohttp
import requests

class BackendResponseException(Exception):
    pass

class ClientRequestException(Exception):
    pass

async def make_request(query: str, api_key: str, sources: list, mode: str, dates: tuple = None):
    url = f'https://api.ditto.fyi/get/raw_query?q={query}&s={",".join(sources)}&m={mode}'

    if dates[0] and dates[1]:
        url += f'&sd={dates[0]}&ed={dates[1]}'

    try:
      headers = {'X-API-Key': api_key}
      async with aiohttp.ClientSession() as session:
          async with session.get(url, headers=headers) as response:
              if response.status == 200:
                  data = await response.json()
                  return data
              elif response.status == 400:
                  raise BackendResponseException("Bad Request: Check your request parameters.")
              elif response.status == 401:
                  raise BackendResponseException("Unauthorized: Invalid Credentials, check your API key")
              else:
                  raise BackendResponseException(f"Server error: {response.status}")
    except aiohttp.ClientError as e:
        raise ClientRequestException(f"Request failed {e}")

def make_sync_request(query: str, api_key: str, sources: list, mode: str, dates: tuple = None): 
    url = f'https://api.ditto.fyi/get/raw_query?q={query}&s={",".join(sources)}&m={mode}'

    if dates and dates[0] and dates[1]:
        url += f'&sd={dates[0]}&ed={dates[1]}'

    try:
        headers = {'X-API-Key': api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 400:
            raise BackendResponseException("Bad Request: Check your request parameters.")
        elif response.status_code == 401:
            raise BackendResponseException("Unauthorized: Invalid Credentials, check your API key")
        else:
            raise BackendResponseException(f"Server error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ClientRequestException(f"Request failed {e}")
