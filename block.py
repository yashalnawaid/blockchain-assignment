from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json

from blockchain_types import BlockData, BlockIndex, HashStr, TimestampStr


@dataclass
class Block:
    """Represents a single block in the blockchain."""

    index: BlockIndex
    timestamp: TimestampStr
    data: BlockData
    previous_hash: HashStr
    hash: HashStr = field(init=False)

    def __post_init__(self) -> None:
        self.hash = self.compute_hash()

    def compute_hash(self) -> HashStr:
        payload = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
        }

        block_string = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")

        return hashlib.sha256(block_string).hexdigest()

    @classmethod
    def create_genesis(cls, data: BlockData | None = None) -> "Block":
        timestamp = datetime.now(timezone.utc).isoformat()
        return cls(
            index=0,
            timestamp=timestamp,
            data=data if data is not None else "Genesis Block",
            previous_hash="0" * 64,
        )

    @classmethod
    def create_next(cls, previous_block: "Block", data: BlockData) -> "Block":
        timestamp = datetime.now(timezone.utc).isoformat()
        return cls(
            index=previous_block.index + 1,
            timestamp=timestamp,
            data=data,
            previous_hash=previous_block.hash,
        )

