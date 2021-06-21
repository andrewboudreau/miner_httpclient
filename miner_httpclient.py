
import json
import logging
import requests

# since i'm a newb, pip install "jsonrpcclient[requests]"
from jsonrpcclient import request
from jsonrpcclient.exceptions import ReceivedErrorResponseError
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request

logger = logging.getLogger(__name__)

# miner http api reference code
## https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc

class Client:
    a = "1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw"
    
    def __init__(self, scheme="http", host="localhost", port="4467"):
        self.url = f'{scheme}://{host}:{port}/jsonrpc'
        self.client = HTTPClient(self.url, basic_logging=True)

    def http_post(self, method, **kwargs):
        try:
          return self.client.send(Request(method, kwargs))
        except ReceivedErrorResponseError as ex:
            return ex #logging.error("%d: %s", ex.data.id, response.data.message)
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

    # ledger
    def ledger_balance(self, address=None):
        if address is None:
          return self.http_post("ledger_balance") 
        else:
          return self.http_post("ledger_balance", address=address)
    
    #def ledger_balance(self, htlc=True):
    #  return False

    def ledger_gateways(self, verbose=False):
        return self.http_post("ledger_gateways")

    def ledger_validators(self):
         return self.http_post("ledger_validators")

    def ledger_variables(self, name=None):
         return self.http_post("ledger_variables")

    # peer
    def peer_session(self):
        return self.http_post("peer_session")

    def peer_listen(self):
        return self.http_post("peer_listen")

    def peer_addr(self):
        return self.http_post("peer_addr")

    def peer_connect(self, address):
        return self.http_post("peer_connect")

    def peer_ping(self, address):
        return self.http_post("peer_ping")

    def peer_book(self, address):
        return self.http_post("peer_book")

    def peer_gossip_peers(self):
        return self.http_post("peer_gossip_peers")

    def peer_refresh(self, address=None):
        return self.http_post("peer_refresh")

   # state channel
    def sc_active(self):
        return self.http_post("sc_active")

    def sc_list(self):
        return self.http_post("sc_list")

    # snapshot
    def snapshot_list(self):
        return self.http_post("snapshot_list")

    # transaction
    def snapshot_list(self):
        return self.http_post("snapshot_list")

    # transactions

# txn_queue(self)
# txn_add_gateway(self, owner)
# txn_assert_location(self, {owner, location})

# transaction_get(self, hash)
 # 1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw