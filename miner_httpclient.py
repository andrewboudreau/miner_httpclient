
import json
import logging
import requests

# since i'm a newb, pip install "jsonrpcclient[requests]"
from jsonrpcclient import request
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request

logger = logging.getLogger(__name__)

# miner http api reference code
## https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc

class Client:
    def __init__(self, scheme="http", host="localhost", port="4467"):
        self.url = f'{scheme}://{host}:{port}/jsonrpc'
        self.client = HTTPClient(self.url, basic_logging=True)

    def http_post(self, method, **kwargs):
        print(kwargs)
        response = self.client.send(Request(method, kwargs))
        if response.data.ok:
          print(response.data.result)
          return response.data.result
        else:
          logging.error(response.data.message)
          return None

    # account
    def account(self, address="1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw"):
        return self.client.request("account_get", address=address)
    
    # blocks
    def block_height(self):
        return self.http_post("block_height")
    
    def block(self, height=None):
        if height is None:
          return self.http_post("block_get") 
        else:
          return self.http_post("block_get", height=height)

    #def blockForHash(self, hash):
        # not sure what to do here
    
    # dkg
    def dkg_status(self):
        return self.http_post("dkg_status")
        
    def dkg_queue(self):
        return self.http_post("dkg_queue")
    
    def dkg_next(self):
        return self.http_post("dkg_next")
    
    def dkg_running(self):
        return self.http_post("dkg_running")


    # hbbft
    def hbbft_status(self):
        return self.http_post("hbbft_status")

    def hbbft_queue(self):
        return self.http_post("hbbft_queue")

    def hbbft_skip(self):
        return self.http_post("hbbft_skip")

    # info
    def info_height(self):
        return self.http_post("info_height")
    
    def info_in_consensus(self):
        return self.http_post("info_in_consensus")["in_consensus"]
    
    def info_name(self):
        return self.http_post("info_name")
    
    def info_block_age(self):
        return self.http_post("info_block_age")
    
    def info_p2p_status(self):
        return self.http_post("info_p2p_status")
    
    def info_region(self):
        return self.http_post("info_region")
    
    def info_summary(self):
        return self.http_post("info_summary")

 # 1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw