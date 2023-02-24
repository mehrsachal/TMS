import web3 as w3
# define the wallet credentials
private_key = "6514f7a2587c45a5f938c999f9662d8476a344ebacdb36249c349e45a1d494fd"
wallet_address = "0xa69DFece7a990B8C4A85515F62A824B5F960b90E"

# create an account object from the private key
account = w3.eth.account.from_key(private_key)

# get the current transaction count for the wallet address
nonce = w3.eth.get_transaction_count(wallet_address)

# function to add a new IPFS hash to the contract
def add_hash(key, value):
    # build the transaction
    tx = contract.functions.sendHash(key, value).buildTransaction({
        "from": wallet_address,
        "gas": 1000000,
        "gasPrice": w3.toWei("10", "gwei"),
        "nonce": nonce,
    })

    # sign the transaction with the account
    signed = account.sign_transaction(tx)

    # send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    # wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # check the transaction status
    if receipt["status"] == 1:
        print("Hash added successfully!")
    else:
        print("Failed to add hash.")
