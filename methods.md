 
  ```erlang 
  % # docker exec -it validator miner remote_console
   miner_jsonrpc_blocks:handle_rpc(<<"block_get">>, #{<<"height">> => 904612}).
```

```bash
 curl 
 -H 'Content-Type: application/json-rpc' 
 -d '{"jsonrpc":"2.0","id":1,"method":"block_get", "params":{"height":904612}}' 
 http://127.0.0.1:4467
```

# [account](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_accounts.erl)
 - def account_get(self, address)

# [blocks](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_blocks.erl)
 - def block_height(self)
 - def block_get(self, height=None)

# [info](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_info.erl)
 - def info_height(self)
 - def info_in_consensus(self) 
 - def info_name(self)
 - def info_block_age(self)
 - def info_p2p_status(self) 
 - def info_region(self)
 - def info_summary(self)
 - def blockForHash(self, hash)

# [dkg](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_dkg.erl)
 - def dkg_status(self)
 - def dkg_queue(self)
 - def dkg_next(self)
 - def dkg_running(self)

# [hbbft](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_hbbft.erl)
 - def hbbft_status(self)
 - def hbbft_queue(self)
 - def hbbft_skip(self)

# [ledger](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_ledger.erl)
 - def ledger_balance(self, address=None)
 - def ledger_balance(self, htlc=True)
 - def ledger_gateways(self, verbose=False)
 - def ledger_validators(self)
 - def ledger_variables(self, name=None)

# [peer](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_peer.erl)
  - def peer_session(self)
  - def peer_listen(self)
  - def peer_addr(self)
  - def peer_connect(self, address)
  - def peer_ping(self, address)
  - def peer_book(self, address)
  - def peer_gossip_peers(self)
  - def peer_refresh(self, address=None)
    
# [state channel](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_sc.erl)
 - def sc_active(self)
 - def sc_list(self)

# [snapshot](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_snapshot.erl)
 - def snapshot_list(self)

# [txn](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txn.erl)
 - def txn_queue(self)
 - def txn_add_gateway(self, owner)
 - def txn_assert_location(self, owner, location)

# [txns](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txns.erl)
- def transaction_get(self, hash)