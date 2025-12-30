import financedatabase as fd
from positions import PositionsTable, Position

def get_positions_split(table: PositionsTable):

    for position in table.positions:

        symbol = position.symbol

    return dict