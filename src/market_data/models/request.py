from dataclasses import dataclass

from .time_range import TimeRange


@dataclass(frozen=True, slots=True)
class MarketDataRequest:
    symbol: str
    period: TimeRange
    interval: str | None = None

    def __post_init__(self) -> None:
        if not self.symbol:
            raise ValueError("symbol must not be empty")
