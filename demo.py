from __future__ import annotations

import logging

from blockchain import Blockchain


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def run_demo() -> None:
    logger = logging.getLogger("demo")

    logger.info("Starting blockchain demo.")
    chain = Blockchain()

    logger.info("Adding demo blocks to the chain.")
    chain.add_block({"sender": "Alice", "receiver": "Bob", "amount": 10})
    chain.add_block({"sender": "Bob", "receiver": "Charlie", "amount": 5})
    chain.add_block({"sender": "Charlie", "receiver": "Dana", "amount": 2})

    print("\n=== Original Blockchain ===")
    chain.pretty_print()
    print(f"Is blockchain valid? {chain.is_valid()}")

    logger.info("Tampering with data in an earlier block.")
    
    block_to_tamper = chain._chain[1]  
    block_to_tamper.data = {"sender": "Alice", "receiver": "Bob", "amount": 1000}

    print("\n=== Tampered Blockchain ===")
    chain.pretty_print()
    print(f"Is blockchain valid after tampering? {chain.is_valid()}")

    logger.info("Blockchain demo finished.")


if __name__ == "__main__":
    configure_logging()
    run_demo()

