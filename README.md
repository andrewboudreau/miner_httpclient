# Usage & Notes
An [http client](https://github.com/andrewboudreau/miner_httpclient) written in Python makes requesting data from the [Helium miner](https://github.com/helium/miner/) jsonrpc endpoints easier.

```python
# Create a client (only logs errors)
client = Client()
summary = client.info_summary()
print(f'Your miner "{summary["name"]}" has an uptime of {summary["uptime"]}')

# Create a new client with more verbose logging and non-default configs
client = Client(scheme="http", host="localhost", port=4467, logging=True)
```

Since the python client is an http client wrapper, it does the same thing as `curl` but makes life a little easier. All of the calls can be made over `curl` using this simple example.
```bash
 curl 
 -H 'Content-Type: application/json-rpc' 
 -d '{"jsonrpc":"2.0","id":1,"method":"block_get", "params":{"height":904612}}' 
 http://127.0.0.1:4467
```

The JSON prc handlers are implemented in Erlang and can also be called directly from the `remote console` as seen in the following example.
```erlang 
  % # docker exec -it validator miner remote_console
  miner_jsonrpc_blocks:handle_rpc(<<"block_get">>, #{<<"height">> => 904612}).
```

# API Endpoints


## [account](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_accounts.erl)
 - ✅ account_get(address)
  ```python
    c = Client()
    addr = c.peer_addr()
    c.account_get(addr)
  ```

## [blocks](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_blocks.erl)
 - ✅ block_height()
 - ✅ block_get(height=None, hash=None)
 ```python
    c = Client()
    height = c.block_height()
    c.block_get(height)
    
  ```

## [info](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_info.erl)
 - ✅ info_height()
 - ✅ info_in_consensus() 
 - ✅ info_name()
 - ✅info_block_age()
 - ❌ info_p2p_status() 
 - ❌ info_region()
 - ✅ info_summary()
 
## [dkg](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_dkg.erl)
 -  dkg_status()
 -  dkg_queue()
 -  dkg_next()
 -  dkg_running()

## [hbbft](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_hbbft.erl)
 -  hbbft_status()
 -  hbbft_queue()
 -  hbbft_skip()

## [ledger](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_ledger.erl)
 -  ledger_balance(address=None)
 -  ledger_balance(htlc=True)
 -  ledger_gateways(verbose=False)
 -  ledger_validators()
 -  ledger_variables(name=None)

## [peer](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_peer.erl)
  -  peer_session()
  -  peer_listen()
  -  peer_addr()
  -  peer_connect(address)
  -  peer_ping(address)
  -  peer_book(address)
  -  peer_gossip_peers()
  -  peer_refresh(address=None)
    
## [state channel](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_sc.erl)
 -  sc_active()
 -  sc_list()

## [snapshot](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_snapshot.erl)
 - snapshot_list()

## [txn](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txn.erl)
 -  txn_queue()
 -  txn_add_gateway(owner)
 -  txn_assert_location(owner, location)

## [txns](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txns.erl)
-  transaction_get(hash)