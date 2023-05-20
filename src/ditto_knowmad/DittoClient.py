import asyncio
from enum import Enum

from .backend_requests import make_request, make_sync_request, make_handle_request, make_sync_handle_request

class ApiKeyException(Exception):
    pass

class DittoClient():
    def __init__(self, api_key):
        self.api_key = api_key

    def get_posts_from_source(self, query: str, sources: list, sync=False) -> object:
        if not self.api_key:
            raise ApiKeyException("No API Key was set when instantiating DittoClient object.")
        
        if sync:
            print("Waiting on API...")
            response = make_sync_request(query=query, sources=sources, api_key=self.api_key)
        else:
            response = asyncio.run(make_request(query=query, sources=sources, api_key=self.api_key))

        return response

    def get_tweets_by_handle(self, query: str, sync=False) -> object:
        if not self.api_key:
                raise ApiKeyException("No API Key was set when instantiating DittoClient object.")
        
        if sync:
            print("Waiting on API...")
            response = make_sync_handle_request(query=query, api_key=self.api_key)
        else:
            response = asyncio.run(make_handle_request(query=query, api_key=self.api_key))

        return response
