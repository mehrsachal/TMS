# import the web3 library
import web3
import json

# define the contract address and the wallet address
CONTRACT_ADDRESS = "0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8"
WALLET_ADDRESS = "0xd4B00887F56646A009385Bc313869762A3E958Bf"

# connect to the Ethereum network
w3 = web3.Web3(web3.Web3.HTTPProvider("https://goerli.infura.io/v3/0776cf37dfb04efdacd478388c7c1dec"))

# load the contract ABI
with open("abi.json") as file:
    abi = json.load(file)

# create a contract instance
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# define the wallet credentials
PRIVATE_KEY = "140ac9264a526d5ed009a5964d259f30ec92f3015a4e2fd1da5e42430886a83d"

# create an account object from the private key
account = w3.eth.account.from_key(PRIVATE_KEY)


def add_ipfs_hash(key, value):
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    tx_dict = contract.functions.addHash(key, value).buildTransaction({
        'chainId': chain_id,
        'gas': 70000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(tx_dict, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt.transactionHash



def get_hash(key):
    # call the contract function and return the result
    return contract.functions.getHash(key).call()


if __name__ == '__main__':
    # example usage
    key = 'some_key'
    value = 'some_value'

    # add a new hash to the contract
    tx_hash = add_ipfs_hash(key, value)
    print(f'Transaction hash: {tx_hash.hex()}')

    # get the value of the hash from the contract
    hash_value = get_hash(key)
    print(f'Hash value: {hash_value}')
