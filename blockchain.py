from __future__ import annotations

from typing import Iterable, List
import logging

from blockchain_types import BlockData
from block import Block


logger = logging.getLogger(__name__)


class Blockchain:
    """Simple in-memory blockchain without mining or proof-of-work."""

    def __init__(self) -> None:
        logger.info("Initializing blockchain with genesis block.")
        self._chain: List[Block] = [Block.create_genesis()]

    @property
    def chain(self) -> List[Block]:
        return list(self._chain)

    @property
    def last_block(self) -> Block:
        return self._chain[-1]

    def add_block(self, data: BlockData) -> Block:
        logger.info("Adding new block to blockchain.")
        new_block = Block.create_next(self.last_block, data)
        self._chain.append(new_block)
        logger.info("Block added successfully.")
        return new_block

    def is_valid(self) -> bool:
        logger.info("Validating entire blockchain.")

        if not self._chain:
            logger.warning("Blockchain is empty during validation.")
            return False

        genesis = self._chain[0]
        if genesis.index != 0:
            logger.error("Genesis block has invalid index.")
            return False
        if genesis.previous_hash != "0" * 64:
            logger.error("Genesis block has invalid previous_hash.")
            return False
        if genesis.hash != genesis.compute_hash():
            logger.error("Genesis block hash does not match computed hash.")
            return False

        for i in range(1, len(self._chain)):
            current = self._chain[i]
            previous = self._chain[i - 1]

            if current.hash != current.compute_hash():
                logger.error(
                    "Block at index %s has an invalid hash.", current.index
                )
                return False

            if current.previous_hash != previous.hash:
                logger.error(
                    "Block at index %s has invalid previous_hash link.",
                    current.index,
                )
                return False

            if current.index != previous.index + 1:
                logger.error(
                    "Block indices are not sequential at index %s.",
                    current.index,
                )
                return False

        logger.info("Blockchain validation succeeded.")
        return True

    def __iter__(self) -> Iterable[Block]:
        return iter(self._chain)

    def __len__(self) -> int:
        return len(self._chain)

    def pretty_print(self) -> None:
        for block in self._chain:
            print("-" * 40)
            print(f"Index       : {block.index}")
            print(f"Timestamp   : {block.timestamp}")
            print(f"Data        : {block.data}")
            print(f"Prev. Hash  : {block.previous_hash}")
            print(f"Hash        : {block.hash}")
        print("-" * 40)

