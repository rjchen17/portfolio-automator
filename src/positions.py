"""Classes pertaining to positions, which include methods for loading and transforming data."""

import os
from dataclasses import dataclass
from pathlib import Path
from constants.configuration import SCHWAB_COLUMNS, SECURITY_TYPES


class Position:
    """A position of a single security.

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

    def __init__(
        self,
        symbol: str,
        quantity: float | str,
        price: float | str,
        cost_basis: float | str,
        security_type: str | None = None,
        name: str | None = None,
    ):
        self.symbol = symbol

        if not isinstance(quantity, float):
            self.float = float(quantity)
        else:
            self.float = float

        if not isinstance(price, float):
            self.price = Position.from_dollar_amount(price)
        else:
            self.price = price

        if not isinstance(cost_basis, float):
            self.cost_basis = Position.from_dollar_amount(cost_basis)
        else:
            self.cost_basis = cost_basis

        if security_type not in SECURITY_TYPES:
            raise ValueError(f"Security type {security_type} must be one of f{SECURITY_TYPES}. ")
        else:
            self.security_type = security_type

        self.quantity = int(quantity)
        self.name = name

    @staticmethod
    def from_dollar_amount(amount: str) -> float:
        """Returns a float dollar amount given a string. """
        try:
            dollar_amount = float(amount.strip().replace("$", ""))
        except ValueError:
            raise ValueError(f"Provided {amount} is not a valid dollar amount")
        return dollar_amount


class PositionsTable:
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

        with open(path, 'r') as positions_table:

            data = positions_table.readlines()
            data.pop(0)  # Remove account number and data header
            data.pop(0)  # Remove blank line
            columns = data.pop(0).strip()  # Remove column names, save for data validation

            if columns != SCHWAB_COLUMNS:
                raise ValueError("Incorrect column names. Ensure that data has not been modified/corrupted. If data"
                                 " is correct, code format is out of date and must be patched. ")

            positions = []
            for position in data:
                position = position.split(",")
                position = [info.replace('"', '') for info in position]
                position = Position(symbol=position[0], name=position[1], quantity=position[2],
                                    price=position[3], cost_basis=position[10])
                positions.append(position)

            return cls(positions)

#a = PositionsTable.load_from_schwab("../dummy_schwab.csv")