import aiohttp
import requests

class BackendResponseException(Exception):
    pass

class ClientRequestException(Exception):
    pass

async def make_request(query: str, api_key: str, sources: list):
    try:
      headers = {'X-API-Key': api_key}
      async with aiohttp.ClientSession() as session:
          async with session.get(f'https://api.ditto.fyi/get/raw_query?q={query}&s={",".join(sources)}', headers=headers) as response:
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

def make_sync_request(query: str, api_key: str, sources: list): 
    try:
        headers = {'X-API-Key': api_key}
        response = requests.get(f'https://api.ditto.fyi/get/raw_query?q={query}&s={",".join(sources)}', headers=headers)
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
    
async def make_handle_request(query: str, api_key: str):
    try:
      headers = {'X-API-Key': api_key}
      async with aiohttp.ClientSession() as session:
          async with session.get(f'https://api.ditto.fyi/get/by_twitter_handle?q={query}', headers=headers) as response:
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
            
