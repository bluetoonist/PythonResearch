from dataclasses import dataclass
from typing import Optional


@dataclass
class Bun:
    reference_id: str


def dispense_bun(with_none=True) -> Optional[Bun]:
    if with_none:
        return None

    return Bun(reference_id="What")
