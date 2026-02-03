
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

ALCHEMY = os.getenv("ALCHEMY_URL")
PRIVATE_KEY = os.getenv("GAME_WALLET_KEY")
HCX_TOKEN = "0x95e3442699f4e3c8d9fdf78d2a3918203c9d7cf2"

w3 = Web3(Web3.HTTPProvider(ALCHEMY))

abi = [{
    "constant": False,
    "inputs": [{"name": "_to", "type": "address"},{"name": "_value", "type": "uint256"}],
    "name": "transfer",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
}]

def reward_player(player_wallet, amount_hcx):
    account = w3.eth.account.from_key(PRIVATE_KEY)
    contract = w3.eth.contract(address=HCX_TOKEN, abi=abi)

    nonce = w3.eth.get_transaction_count(account.address)

    tx = contract.functions.transfer(
        player_wallet,
        int(amount_hcx * 10**18)
    ).build_transaction({
        'chainId': 1,
        'gas': 200000,
        'gasPrice': w3.to_wei('30', 'gwei'),
        'nonce': nonce,
    })

    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Reward sent:", w3.to_hex(tx_hash))
