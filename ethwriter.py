# import the web3 library
import web3
import json

# define the contract address
contract_address = "0x9535eF5c9fEB73110Abd3AD6E9b8a18DCca01b6A"

# connect to the Ethereum network
w3 = web3.Web3(web3.Web3.HTTPProvider("https://sepolia.infura.io/v3/0776cf37dfb04efdacd478388c7c1dec"))

# load the contract ABI
with open("abi.json") as file:
    abi = json.load(file)

# create a contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# define the wallet credentials
private_key = "6514f7a2587c45a5f938c999f9662d8476a344ebacdb36249c349e45a1d494fd"
wallet_address = "0xa69DFece7a990B8C4A85515F62A824B5F960b90E"
nonce = w3.eth.getTransactionCount(wallet_address)

# unlock the wallet
w3.eth.account.privateKeyToAccount(private_key)

# function to add a new IPFS hash to the contract
def add_hash(key, value):
    # build the transaction
    tx = contract.functions.sendHash(key, value).buildTransaction({
        "from": wallet_address,
        "gas": 1000000,
        "gasPrice": w3.toWei("10", "gwei"),
        "nonce": nonce,
    })

    # sign the transaction
    signed = w3.eth.account.signTransaction(tx, private_key=private_key)

    # send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    # wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # check the transaction status
    if receipt["status"] == 1:
        print("Hash added successfully!")
    else:
        print("Failed to add hash.")

# function to retrieve an IPFS hash from the contract
def get_hash(key):
    # call the getHash function
    result = contract.functions.getHash(key).call()

    # return the result
    return result
key = "bafybeiadjpljqfre5zb6xhpknl5kuyvssvhzbrkbn3j3eyhgtdsdssdthi"

# add a new IPFS hash to the contract
add_hash("1", "a")

# retrieve an IPFS hash from the contract
value = get_hash("1")
print(value)
