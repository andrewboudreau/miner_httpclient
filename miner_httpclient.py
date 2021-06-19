
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
        print(response.status_code)
        return response.json()

    # account

    # blocks
    def block_height(self):
        return self.http_post("block_height")["result"]
    
    def block(self, height=None):
        if height is None:
          return self.http_post("block_get") 
        else:
          return self.http_post("block_get", height)

    #def blockForHash(self, hash):
        # not sure what to do here
    

        

 # 1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw