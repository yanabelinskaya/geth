from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3 .middleware_onion.inject(geth_poa_middleware, layer=0)

contract= w3.eth.contract(address=contract_address,abi=abi)

print(contract.address)

print(f"Баланс смарт контракта: {w3.eth.get_balance(contract.address)}")
print(f"Баланс первого аккаунта: {w3.eth.get_balance('0xFC5724b8da0C10ec2bE84b0962B32E8073c8eFD5')}")
print(f"Баланс второго аккаунта: {w3.eth.get_balance('0xB8b107594141FBfb9f64B51590F805c3576E8c12')}")
print(f"Баланс третьего аккаунта: {w3.eth.get_balance('0xDdd3B40c7D4E61832209377B5D6d61cB1278c525')}")
print(f"Баланс четвертого аккаунта: {w3.eth.get_balance('0x8Ee3CF32BdF95Ad7DDDd0f60Ae903be7f5B0A8A4')}")
print(f"Баланс пятого аккаунта: {w3.eth.get_balance('0xcd47fD5C1B1a5236492089f18049F38FA2089d16')}")