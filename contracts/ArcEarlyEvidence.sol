// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title ArcEarlyEvidence
/// @notice Minimal immutable proof that BiX Arc Early Intelligence is running on Arc Mainnet.
contract ArcEarlyEvidence {
    string public constant project = "BiX Arc Early Intelligence";
    bytes32 public immutable genesisEvidence;
    uint256 public immutable deployedAt;

    constructor(bytes32 evidenceHash) {
        genesisEvidence = evidenceHash;
        deployedAt = block.timestamp;
    }
}
