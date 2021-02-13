import pandas as pd
from pandas import DataFrame

def read_input() -> DataFrame:
    """Reads the ATMVol csv file and returns it as dataframe."""
    df = pd.read_csv('app/data/ATMVol.csv')
    df = df.fillna(0.0)
    return df

def filter_data(input_data, column_name, value) -> DataFrame:
    """Filters a dataframe by a specific column and value"""

    indices = list(input_data[input_data[column_name] == value].index.values)
    return input_data.loc[indices, :]

## --- example of use ---

# df = read_input()

# Selecting data with only Expiry Time == 30
# choose between 30.0,  60.0,  90.0, 120.0, 150.0, 180.0
# expiry = 30.0
# data_selected = filter_data(df, "ExpiryTime", expiry)