
import json
import logging
import requests

# since i'm a newbie, pip install "jsonrpcclient[requests]"
from jsonrpcclient import request
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.exceptions import ReceivedErrorResponseError
from jsonrpcclient.requests import Request

logger = logging.getLogger(__name__)

# miner http api reference code
## https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc

class Client:
    a = "1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw"
    
    def __init__(self, scheme="http", host="localhost", port="4467", logging=False):
        self.url = f'{scheme}://{host}:{port}/jsonrpc'
        self.client = HTTPClient(self.url, basic_logging=logging)

    def http_post(self, method, **kwargs):
        try:
          return self.client.send(Request(method, kwargs))
        except ReceivedErrorResponseError as ex:
            logging.error(" id: %d method: '%s' message: %s", ex.response.id, method, ex.response.message)

    # account
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_accounts.erl
    def account_get(self, address="1YSY5aooEh3LEt7sxDt1xdqw4cUd1gpwztQKE1fPsGRDozmJ2sw"):
        return self.client.request("account_get", address=address)
    
    # blocks
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_blocks.erl
    def block_height(self):
        return self.http_post("block_height")
    
    def block_get(self, height=None):
        if height is None:
          return self.http_post("block_get") 
        else:
          return self.http_post("block_get", height=height)

    #def blockForHash(self, hash):
        # not sure what to do here
    
    # dkg
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_dkg.erl
    def dkg_status(self):
        return self.http_post("dkg_status")
        
    def dkg_queue(self):
        return self.http_post("dkg_queue")
    
    def dkg_next(self):
        return self.http_post("dkg_next")
    
    def dkg_running(self):
        return self.http_post("dkg_running")


    # hbbft
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_hbbft.erl
    def hbbft_status(self):
        return self.http_post("hbbft_status")

    def hbbft_queue(self):
        return self.http_post("hbbft_queue")

    def hbbft_skip(self):
        return self.http_post("hbbft_skip")

    # info
    # # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_info.erl
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
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_ledger.erl
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
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_peer.erl
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
   # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_sc.erl
    def sc_active(self):
        return self.http_post("sc_active")

    def sc_list(self):
        return self.http_post("sc_list")

    # snapshot
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_snapshot.erl
    def snapshot_list(self):
        return self.http_post("snapshot_list")

    # txn
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_txn.erl
    def txn_queue(self):
        return self.http_post("txn_queue")

    def txn_add_gateway(self, owner):
        return self.http_post("txn_add_gateway", owner)

    def txn_assert_location(self, owner, location):
        return self.http_post("txn_assert_location", owner=owner, location=location)

    # txns
    # https://github.com/helium/miner/blob/mra/jsonrpc/src/jsonrpc/miner_jsonrpc_txns.erl
    def transaction_get(self, hash):
        return self.http_post("transaction_get", hash=hash)
