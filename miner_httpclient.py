import json
import logging

logger = logging.getLogger(__name__)


class Client:
    def __init__(self, scheme="http", host="localhost", port="4467"):
        self.url = f'{scheme}://{host}:{port}/jsonrpc'

    def build_payload(method, params=[""]):
        return {
            "jsonrpc": "2.0",
            "id":1,
            "method": method,
            "params": params
        }

        

    