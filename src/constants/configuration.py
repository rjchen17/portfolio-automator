"""Shared constant values. """

# >>> Data Validation

SCHWAB_COLUMNS = ('"Symbol","Description","Qty (Quantity)","Price","Price Chng $ (Price Change $)","Price Chng % (Price '
                  'Change %)","Mkt Val (Market Value)","Day Chng $ (Day Change $)","Day Chng % '
                  '(Day Change %)","Cost Basis","Gain $ (Gain/Loss $)","Gain % (Gain/Loss %)","Reinvest?",'
                  '"Reinvest Capital Gains?","Security Type",')

# <<< Data Validation

# >>> Position data

SPLITS = ["dom", "intl", "fi"]  # Supported asset allocation "bins"
SECURITY_TYPES = ["eq", "mm", "etf", "mf"]

# <<< Position data