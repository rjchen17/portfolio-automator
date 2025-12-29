"""Classes pertaining to positions, which include methods for loading and transforming data."""

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Position:
    """ A position of a single security.

    Attributes:
        symbol: The ticker symbol (i.e. abbreviation) for the underlying security.
        quantity: The amount of the share owned. Certain security types support
          decimal quantities (e.g. mutual funds), while others don't (e.g. ETFs).
        price: The current price, per share, of the security.
        cost_basis: The total cost of the position originally paid by the holder.
        security_type: The type of security (e.g. mutual fund, money market), used for trading purposes, as certain
          securities can only be bought and sold in only integer quantities.
        name: The full name of the security. Only necessary for visualization/printing purposes.
    """
    symbol: str
    quantity: float
    price: float
    cost_basis: int
    security_type: str | None = None
    name: str | None = None


class PositionTable:
    """
    The full table of positions held by an investor.
    """
    def __init__(self, positions: list[Position]):

        self.positions = positions

    @classmethod
    def load_from_schwab(cls, path: str | Path):
        """ Loads a position table from a Schwab exported file.

        Args:
            path: Path to the .csv positions file.

        """

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found at path: {path}. ")

