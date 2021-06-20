# miner_httpclient

The helium miner is getting a [JSON RPC API](https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc) over `HTTP:4467`. Here I present a python client in the hopes to make other things easier

# Usage
```python
>>> Client().info_in_consensus()
False
>>> Client().block_height()
```

# Todo
 - learn python (ok yeah sure... doing that)
- *PARAMS*, wait for code fixes, thanks evan.

~~ - *PARAMS*, json rpc params into erlang handlers (HOW, one example of this working solves them all)
   - tried json, tuples, dictionary, lists, and various other inputs but only to get `invalid request` or `method not found`
   - if i had to be it's really easy and only challenge is my lack of knowledge here ~~
 - figure out simple error handling
 - use a library [jsonrpcclient](https://jsonrpcclient.readthedocs.io/en/latest/api.html), seems fine so far. 
 - loose json result sets or do we want typed results for the results?
 - get the rest of the [api surface](https://github.com/helium/miner/tree/mra/jsonrpc/src/jsonrpc) implemented
 - how other people write api clients in python [SendGrid](https://github.com/sendgrid/sendgrid-python)
 - create an [open-rpc document](https://spec.open-rpc.org/#introduction) for the miner 
   - after this everyone can win, this feels like the grand finale.
