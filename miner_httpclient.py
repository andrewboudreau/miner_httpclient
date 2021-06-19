
import json
import logging
import requests

logger = logging.getLogger(__name__)

# miner http api reference code
## https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc

class Client:
    def __init__(self, scheme="http", host="localhost", port="4467"):
        self.url = f'{scheme}://{host}:{port}/jsonrpc'

    def jsonrpc_payload(self, method, params):
        return {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params
        }
    
    def http_post(self, method, data=[""]):
        response = requests.post(self.url, json=self.jsonrpc_payload(method, data))
        return response.json()["result"]

    # accountq

    # blocks
    def block_height(self):
        return self.http_post("block_height")
    
    def block(self, height=None):
        if height is None:
          return self.http_post("block_get") 
        else:
          return self.http_post("block_get", height)

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
        return self.http_post("info_in_consensus")
    
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