import asyncio
from enum import Enum
import os 

from .backend_requests import make_request, make_sync_request

class ApiKeyException(Exception):
    pass

class DittoClient():
    def __init__(self, api_key):
        self.api_key = api_key

    def get_posts_from_source(
            self,
            query: str, 
            sources: list, 
            mode: str = 'posts',
            sync: bool = False,
            dates: list = None
            ) -> object:
        
        if not self.api_key:
            raise ApiKeyException("No API Key was set when instantiating DittoClient object.")
        
        if sync:
            print("Waiting on API...")
            response = make_sync_request(
                query=query, 
                sources=sources, 
                api_key=self.api_key,
                mode=mode,
                dates=dates
                )
        else:
            response = asyncio.run(
                make_request(
                    query=query, 
                    sources=sources, 
                    api_key=self.api_key,
                    mode=mode,
                    dates=dates
                    )
                )

        return response
