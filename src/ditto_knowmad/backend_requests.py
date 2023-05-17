import aiohttp

class BackendResponseException(Exception):
    pass

class ClientRequestException(Exception):
    pass

async def make_request(query: str, api_key: str, sources: list):
    try:
      headers = {'X-API-Key': api_key}
      async with aiohttp.ClientSession() as session:
          async with session.get(f'', headers=headers) as response:
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
        
            