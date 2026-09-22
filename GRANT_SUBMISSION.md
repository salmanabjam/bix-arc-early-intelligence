# Arc Microgrant Submission Draft

Project name: BiX Arc Early Intelligence

Live deployment:
https://salmanabjam.github.io/bix-arc-early-intelligence/

Public repo:
https://github.com/salmanabjam/bix-arc-early-intelligence

Arc Mainnet contract:
https://explorer.arc.io/address/0x489DBC6e44215f18bD07e633174AbA7D9aF18e3c

Short description:
BiX Arc Early Intelligence is a small read-only research prototype that detects unusual early token and wallet activity on Arc Mainnet, records timestamped evidence, and anchors an evidence hash on Arc for independent verification. The current experiment deliberately avoids trading claims: it has tested two real observations, produced one candidate signal, and records false positives and lead time before any larger system is built.

How it uses Arc:
Arc Mainnet is used as the immutable, low-cost evidence layer. The prototype commits the SHA-256 hash of collected signal evidence to an Arc smart contract, creating a verifiable on-chain proof that can later be compared with observed market outcomes.

Current stage:
Working prototype on Arc Mainnet. Public source, live demo, deployed contract, and real evidence are available.
