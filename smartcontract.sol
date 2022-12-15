pragma solidity ^0.6.0;

// import the web3.storage interface
import "https://github.com/web3-interfaces/storage/storage.sol";

// define a contract that implements the web3.storage interface
contract IPFSStorage is web3.storage {
    // define a mapping to store the IPFS hashes
    mapping (bytes32 => bytes32) public hashes;

    // function to add a new IPFS hash to the mapping
    function addHash(bytes32 key, bytes32 value) public {
        // set the value at the given key in the mapping
        hashes[key] = value;
    }

    // function to retrieve an IPFS hash from the mapping
    function getHash(bytes32 key) public view returns (bytes32) {
        // return the value at the given key in the mapping
        return hashes[key];
    }
}
