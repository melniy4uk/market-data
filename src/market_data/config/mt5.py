from dataclasses import dataclass

from .base import BaseConfig


@dataclass(frozen=True, slots=True)
class MT5Config(BaseConfig):
    login: int | None = None
    password: str | None = None
    server: str | None = None
    terminal_path: str | None = None
