// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract CIDHashStorage {

  // Define a mapping to hold the CID hashes.
  mapping(uint256 => bytes32) public cidHashes;

  // Function to add a CID hash to the mapping.
  function addCIDHash(bytes32 _cidHash) public {
    // Get the current number of hashes in the mapping.
    uint256 length = cidHashes.length;

    // Add the provided CID hash to the mapping at the next available index.
    cidHashes[length] = _cidHash;
    // print a message saying done
    return "Done";
  }

  // Function to retrieve a CID hash from the mapping.
  function getCIDHash(uint256 _index) public view returns (bytes32) {
    // Return the CID hash at the specified index in the mapping.
    return cidHashes[_index];

  }
}
