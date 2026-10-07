from dataclasses import dataclass

from .base import BaseConfig


@dataclass(frozen=True, slots=True)
class BybitConfig(BaseConfig):
    api_key: str | None = None
    api_secret: str | None = None
    testnet: bool = False
