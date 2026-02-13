import pandas as pd
from financeService import get_data

stocks = ["VNM"]
start_date = ""
end_date = ""
period = "3mo"


data = get_data(stocks, period)