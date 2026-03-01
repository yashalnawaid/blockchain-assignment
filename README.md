## Basic Blockchain (Without Mining)

This project implements a minimal blockchain in Python to demonstrate:

- **Block structure** (`Block` with index, timestamp, data, previous hash, and hash)
- **Cryptographic hashing** using SHA-256
- **Hash chaining** between blocks
- **Data immutability** and its impact on chain integrity
- **Blockchain validation** and tampering detection

### Files

- `blockchain_types.py`: Shared type aliases used across the project.
- `block.py`: Implementation of the `Block` class and hash computation.
- `blockchain.py`: Implementation of the `Blockchain` class (genesis creation, add block, display, validate).
- `demo.py`: Script that builds a chain, validates it, then tampers with a block and shows validation failure.
- `requirements.txt`: Declares that there are no external dependencies.

### How to Run

1. Ensure you have Python 3.10+ installed.
2. From the project root, run:

```bash
python3 demo.py
```

This will:

- Build a small blockchain.
- Print the original, valid chain.
- Tamper with data in an earlier block.
- Re-run validation and show that the chain is now invalid.

Use the console output and the printed blocks as screenshots for your report.

