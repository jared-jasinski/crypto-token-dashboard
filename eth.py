import re
from web3 import Web3
from web3.exceptions import BadFunctionCallOutput
import dexscreener


def extract_token(string):
    pattern = r'0x[a-fA-F0-9]{40}'
    match = re.search(pattern, string)

    if match:
        w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/7f232511c7a0495aaebb6dc7d9ca3396'))

        # ERC-20 token interface
        erc20_interface = [
            {'constant': True, 'inputs': [], 'name': 'name', 'outputs': [{'name': '', 'type': 'string'}],
             'payable': False, 'stateMutability': 'view', 'type': 'function'},
            {'constant': True, 'inputs': [], 'name': 'symbol', 'outputs': [{'name': '', 'type': 'string'}],
             'payable': False, 'stateMutability': 'view', 'type': 'function'},
            {'constant': True, 'inputs': [], 'name': 'decimals', 'outputs': [{'name': '', 'type': 'uint8'}],
             'payable': False, 'stateMutability': 'view', 'type': 'function'},
            {'constant': True, 'inputs': [{'name': '_owner', 'type': 'address'}], 'name': 'balanceOf',
             'outputs': [{'name': 'balance', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view',
             'type': 'function'}
        ]

        try:
            # Check if the address has the required ERC-20 token functions
            contract = w3.eth.contract(address=Web3.to_checksum_address(match.group(0)), abi=erc20_interface)
            contract.functions.name().call()
            contract.functions.symbol().call()
            contract.functions.decimals().call()
            return match.group(0)
        except BadFunctionCallOutput:
            return False

