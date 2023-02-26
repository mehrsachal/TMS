// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IPFSStorage {
  struct Multihash {
    string digest;
    uint8 hashFunction;
    uint8 size;
  }

  mapping(string => string) private _hashes;

  function addHash(string memory key, string memory value) public {
    require(bytes(key).length > 0, "Key cannot be empty");
    require(bytes(value).length > 0, "Value cannot be empty");
    _hashes[key] = value;
  }

  function getHash(string memory key) public view returns (string memory) {
    require(bytes(key).length > 0, "Key cannot be empty");
    return _hashes[key];
  }

  function removeHash(string memory key) public {
    require(bytes(key).length > 0, "Key cannot be empty");
    delete _hashes[key];
  }
}
