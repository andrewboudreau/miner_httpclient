# Usage & Notes
An [http client](https://github.com/andrewboudreau/miner_httpclient) written in Python makes requesting data from the [Helium miner](https://github.com/helium/miner/) jsonrpc endpoints easier.

Install dependencies:

```bash
pip install -r requirements.txt
```

Then try a script like this to get started:

```python
from miner_client import MinerClient

# Create a client (only logs errors)
client = MinerClient()
summary = client.info_summary()
print(f'Your miner "{summary["name"]}" has an uptime of {summary["uptime"]}')

# Create a new client with more verbose logging and non-default configs
client = MinerClient(scheme="http", host="localhost", port=4467, logging=True)
```

Since the python client is an http client wrapper, it does the same thing as `curl`. All of the calls can be made in `curl` using the following example.
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
  c = MinerClient()
  addr = c.peer_addr()
  c.account_get(addr)
  >>> {
      'address': '19Qaj....',
      'balance': 0,
      'dc_balance': 0,
      'dc_nonce': 0, 
      'nonce': 0, 
      'sec_balance': 0, 
      'sec_nonce': 0
    }
```

## [blocks](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_blocks.erl)
 - ✅ block_height()
 - ✅ block_get(height=None, hash=None)
 ```python
    c = MinerClient()
    height = c.block_height()
    c.block_get(height)
  ```

## [info](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_info.erl)
 - ✅ info_height()
 - ✅ info_in_consensus() 
 - ✅ info_name()
 - ✅ info_block_age()
 - ✅ info_p2p_status() 
 - ❌ info_region()
 - ✅ info_summary()
 - ❌ info_version()

 ```python 
c.info_height()
>>> {'epoch': 23029, 'height': 906272}

c.info_in_consensus()
>>> False

c.info_p2p_status()
>>> {'connected': 'yes', 'dialable': 'yes', 'height': 926887, 'nat_type': 'none'}

c.info_block_age()
>>> 127

c.info_summary()
>>> {
  'block_age': 145, 
  'epoch': 23029, 
  'firmware_version': ".....", 
  'gateway_details': 'undefined', 
  'height': 906273, 
  'mac_addresses': [{'eth0': '024...'}, {'lo': '00000.'}], 
  'name': 'rich-holographic-robin', 
  'peer_book_entry_count': 61765, 
  'sync_height': 906273, 
  'uptime': 78608
}
 ```

## [dkg](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_dkg.erl)
 - ✅ dkg_status()
 - ❌ dkg_queue()
 - ✅ dkg_next()
 - ✅ dkg_running()

 ```python
 c.dkg_status()
 >>> {'status': 'not_running'}

c.dkg_next()
>>> {'blocks_to_election': 23, 'next_election_height': 919363, 'running': False}

 c.dkg_running()
 >>> {'error': 'not running'}
 ```

## [hbbft](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_hbbft.erl)
 - ✅ hbbft_status()
 - ❌ hbbft_queue()
 - ✅ hbbft_skip()
 - ✅ hbbft_perf(address=None)
 - ✅ hbbft_perf("self")

 ```python
c.hbbft_perf()
>>> [
  { 
    'address': '11...kXk', 
    'bba_completions': [2, 24], 
    'last_bba': 22, 
    'last_seen': 0, 
    'name': 'scrawny-ultraviolet-dalmatian', 
    'penalty': [6.090986666603694], 
    'seen_votes': [844, 848], 
    'tenure': [0.9978918650793651]
  }, ...  ]

c.hbbft_perf("self")
>>> [
  { 
    'address': '14...RCw', 
    'bba_completions': [21, 21], 
    'last_bba': 14, 
    'last_seen': 0, 
    'name': 'your-validator-name', 
    'penalty': [2.141286666603694], 
    'seen_votes': [711, 745], 
    'tenure': [0.49942956349206347]
  }, ... ]

c.hbbft_perf("hollow-iron-urchin")
>>> [
  {
    'address': '112eW92d...n', 
    'bba_completions': [21, 21],
    'last_bba': 0, 
    'last_seen': 0, 
    'name': 'hollow-iron-urchin', 
    'penalty': [3.1669273013160346], 
    'seen_votes': [743, 745],
    'tenure': [3.121428571428572]}
  }, ... ]

c.hbbft_status()
>>> 'ok'

c.hbbft_skip()
>>> 'ok'
 ```

## [ledger](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_ledger.erl)
 - ✅ ledger_balance(address=None)
 - ✅ ledger_balance(htlc=True)
 - ✅ ledger_gateways(verbose=False)
 - ✅ ledger_validators(address=None)
 - ✅ ledger_validators("self")
 - ✅ ledger_variables(name=None)

```python
c.ledger_balance("13VsoxfztXYkxaJojVRSvNkzpGk84ues3JSg8Xk9t49tqmz9FSy")
>>> {
  'address': '13VsoxfztXYkxaJojVRSvNkzpGk84ues3JSg8Xk9t49tqmz9FSy', 
  'balance': 480098080087, 
  'nonce': 19}

c.ledger_balance()
>>> ...

c.ledger_balance(htlc=True)
>>> ...

c.ledger_validators()
>>>[
  {'dkg_penalty': '0.00', 
  'last_heartbeat': 910809, 
  'owner_address': '14Nv..Y', 
  'performance_penalty': '0.00', 
  'stake': 0, 
  'status': 'unstaked', 
  'tenure_penalty': '0.00', 
  'total_penalty': '0.00', 
  'version': 1, 
  'name': 'faithful-orange-meerkat'
  }, 
  {'dkg_penalty': '0.00', 
  'last_heartbeat': 910809, 
  'owner_address': '14...4v', 
  ...}]

# just this validator
c.ledger_validators("self")
>>> {....}

c.ledger_validators("13VsoxfztXYkxaJojVRSvNkzpGk84ues3JSg8Xk9t49tqmz9FSy")
>>> {....}

c.ledger_variables("validator_version")
>>> 1

c.ledger_variables()
>>> {
  'poc_v4_prob_no_rssi': '0.5', 
  'poc_addr_hash_byte_count': 8, 
  'min_score': '0.15', 
  'max_antenna_gain': 150, 
  'assert_loc_txn_version': 2, 
  'var_gw_inactivity_threshold': 600, 
  'poc_v4_target_challenge_age': 1000, 
  'price_oracle_refresh_interval': 10, 
  'sc_open_validation_bugfix': 1,
  ...}
```

## [peer](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_peer.erl)
  - ✅ peer_session()
  - ✅ peer_listen()
  - ✅ peer_addr()
  - ✅ peer_connect(address)
  - ✅ peer_connect([])
  - ✅ peer_ping(address)
  - ✅ peer_ping([])
  - ✅ peer_book(address)
  - ✅ peer_book("self")
  - ✅ peer_book("all")
  - ✅ peer_gossip_peers()
  - ✅ peer_refresh(address)

```python
c.peer_addr()
>>> '/p2p/11vpHJq2EiMTZo4pGVA8LKcfscDF6AK5N6acuriSx2xsoYwRqvU'

c.peer_book("self")
>>> [{
  'address': '/p2p/11vpHJq2EiMTZo4pGVA8LKcfscDF6AK5N6acuriSx2xsoYwRqvU', 
  'connection_count': 3, 
  'last_updated': '152.281', 
  'listen_addr_count': 1, 
  'listen_addresses': ['/ip4/20.80.32.209/tcp/2154'], 
  'name': 'rich-holographic-robin', 
  'nat': 'none', 
  'sessions': 
    [
      {'local': '/ip4/17....3/tcp/2154',
       'name': 'upbeat-powder-pig', 
       'p2p': '/p2p/11...NPRiUzT', 
       'remote': '/ip4/92.25.106.141/tcp/44158'},
       {.....}
    ]
  }]

c.peer_session()
>>> [
  {
    'local': '/ip4/172.21.0.3/tcp/2154', 
    'name': 'cheery-slate-mantaray', 
    'p2p': '/p2p/112jn...D5', 
    'remote': '/ip4/174.16.197.84/tcp/44158'
  }, 
  {
    'local': '/ip4/172.21.0.3/tcp/2154', 
    'name': 'brave-peach-anteater', 
    'p2p': '/p2p/112mz...2ZVKd', 
    'remote': '/ip4/135.148.147.186/tcp/2154'
  }, 
  ...]

peers = [*map(lambda s: s["p2p"], c.peer_session())]
c.peer_ping(peers)
>>> [
  {'/p2p/112BZd....vX3': 340}, 
  {'/p2p/112jn2....TD5': 336}, 
  {'/p2p/112o9F....Q8o': 54}, 
  {'/p2p/11JKVf....nx': 16}, 
  {'/p2p/11mck8....sZ': 403}
]

a = '/p2p/112AV...wa''
c.peer_ping(a)
>>> {'/p2p/112AV...wa': 71}

c.peer_connect(c.peer_session()[0]["p2p"])
>>> {'connected': True}
```

## [snapshot](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_snapshot.erl)
 - ✅ snapshot_list()

```python
c.snapshot_list()
>>> [{
  'hash': 'JlYwCLzKqR-xx4TczcqVTlPQ9JRn-eYEzJggfDDv1Bk', 
  'hash_hex': [50, 54, 53, 54, 51, 48, 48, 56, 98, 99, 99, 97, 97, 57, 49, 102, 98, 49, 99, 55, 56, 52, 100, 99, 99, 100, 99, 97, 57, 53, 52, 101, 53, 51, 100, 48, 102, 52, 57, 52, 54, 55, 102, 57, 101, 54, 48, 52, 99, 99, 57, 56, 50, 48, 55, 99, 51, 48, 101, 102, 100, 52, 49, 57], 
  'have_snapshot': True, 
  'height': 900721
  }]
```

## [txns](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txns.erl)
- ✅ transaction_get(hash)

```python
hash = "0omOntPuW053tpeJF_4rC5r479HdALCX7d6msfTveDQ"
c.transaction_get(hash)
>>> {
  'block': 906480, 
  'block_hash': 
  '3V4KaCE9F2QXOI08JVYxSaW5Yq__W0MmkdypMI6K16A', 
  'challenger': '11HGieD9yjd5xFHETzAGdrymfvCJwhvJaC8jkYz92qjSQ45iNu4', 
  'fee': 0, 
  'hash': '0omOntPuW053tpeJF_4rC5r479HdALCX7d6msfTveDQ', 
  'onion_key_hash': 'IF5t_BOTbm0d3yuZz7OMCs1rnhw-rqaaPotGr9_oFCI', 
  'secret_hash': 'tAZRX7JQH92yy-nuGz_t6XlWcgdSaW28Jm5QRUSVR8Y', 
  'type': 'poc_request_v1', 
  'version': 10000002
  }
```

## [txn](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_txn.erl)
 -  txn_queue()
 -  txn_add_gateway(owner)
 -  txn_assert_location(owner, location)

## [state channel](https://github.com/helium/miner/tree/master/src/jsonrpc/miner_jsonrpc_sc.erl)
 -  sc_active()
 -  sc_list()

```
Finding this useful? Help me pay for hosting a testnet instance.
Send me HNT @ 13zLoLWM3S7uPip5Fk9BzshUL82A8HgwvDqJdwJca9mSJ5uzFRn
```