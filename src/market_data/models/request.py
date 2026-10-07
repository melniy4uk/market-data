from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class MarketDataRequest:
    symbol: str
    start: datetime
    end: datetime
    interval: str | None = None

    def __post_init__(self) -> None:
        if not self.symbol:
            raise ValueError("symbol must not be empty")

        if self.start >= self.end:
            raise ValueError("start must be earlier than end")
