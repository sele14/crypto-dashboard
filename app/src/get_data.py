# from src.secrets import API_KEY, SECRET_KEY
# from binance.client import Client

# import os
# import pandas as pd
# import math
# from datetime import timedelta, datetime
# from dateutil import parser

# # Initialise API client
# client = Client(API_KEY, SECRET_KEY)

# # get market depth (order book; bids, asks etc)
# depth = client.get_order_book(symbol='BNBBTC')

# # get all symbol prices
# prices = client.get_all_tickers()

# ## Download Full Price History

# ### CONSTANTS
# binsizes = {"1m": 1, "5m": 5, "1h": 60, "1d": 1440}
# batch_size = 750

# def _minutes_of_new_data(symbol, kline_size, data, source):
#     if len(data) > 0:  old = parser.parse(data["timestamp"].iloc[-1])
#     elif source == "binance": old = datetime.strptime('1 Jan 2017', '%d %b %Y')
#     if source == "binance": new = pd.to_datetime(client.get_klines(symbol=symbol, interval=kline_size)[-1][0], unit='ms')
#     return old, new

# def get_crypto_data(symbol, kline_size, save = False):
#     filename = '%s-%s-data.csv' % (symbol, kline_size)
#     if os.path.isfile(filename): data_df = pd.read_csv(filename)
#     else: data_df = pd.DataFrame()
#     oldest_point, newest_point = _minutes_of_new_data(symbol, kline_size, data_df, source = "binance")
#     delta_min = (newest_point - oldest_point).total_seconds()/60
#     available_data = math.ceil(delta_min/binsizes[kline_size])
#     if oldest_point == datetime.strptime('1 Jan 2015', '%d %b %Y'): print('Downloading all available %s data for %s.' % (kline_size, symbol))
#     else: print('Downloading %d minutes of new data available for %s, i.e. %d instances of %s data.' % (delta_min, symbol, available_data, kline_size))
#     klines = client.get_historical_klines(symbol, kline_size, oldest_point.strftime("%d %b %Y %H:%M:%S"), newest_point.strftime("%d %b %Y %H:%M:%S"))
#     data = pd.DataFrame(klines, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
#     data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
#     if len(data_df) > 0:
#         temp_df = pd.DataFrame(data)
#         data_df = data_df.append(temp_df)
#     else: data_df = data
#     data_df.set_index('timestamp', inplace=True)
#     if save: data_df.to_csv(filename)

#     # clean data
#     df = data_df.drop(columns=['ignore','close_time'])
#     # convert to float 
#     df = df.astype({
#                 i : float for i in df.columns
#             }).round(2)
    
#     # Sort by time
#     df = df.reset_index()
#     df.timestamp = pd.to_datetime(df.timestamp)
#     df = df.sort_values('timestamp', ascending=False)
    
#     # ProperCase columns
#     df = df.rename(columns={
#             i : i.title() for i in df.columns
#         })

#     return df
