from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://sepolia.infura.io/v3/0776cf37dfb04efdacd478388c7c1dec'))
print ("Latest Ethereum block number" , w3.eth.blockNumber)