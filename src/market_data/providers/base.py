from abc import ABC, abstractmethod

from market_data.models.request import MarketDataRequest


class MarketDataProvider(ABC):
    @abstractmethod
    def get_ticks(self, request: MarketDataRequest):
        raise NotImplementedError

    @abstractmethod
    def get_candles(self, request: MarketDataRequest):
        raise NotImplementedError
