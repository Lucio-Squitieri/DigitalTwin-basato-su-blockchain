import requests
import json
from moralis import evm_api

api_key = "okQ3Dg1Ai5QzlNVy1Lk8LQxouNjh4xAXl9LwYHy70hh6fYeFMC8G3HVm9Y46JlzL"
with open('abi.json', 'r') as data:
    abi = json.load(data)


params = {
    "address": "0xC822FF9D5Fc34de437193d80942f5fcfDB43F804",
    "function_name": "fetchIpfs",
    "chain": "goerli",
}
body = {
    "abi": abi,
    "params": params
}

result = evm_api.utils.run_contract_function(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

r = requests.get(result, headers={'Accept': 'application/json'})

datar = r.json()

print(datar["loss"])

# https://ipfs.moralis.io:2053/ipfs/Qmd2iDWBev1VDxmSfTJSGeS1BVh9hqnFnEXe6Dhr4mpDir/modello.json
