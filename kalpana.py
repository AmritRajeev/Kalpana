import numpy as np
import matplotlib as plt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
from sklearn.ensemble import RandomForestClassifier
api_key="MNNSPRF08WG4DTL3"
time_series = TimeSeries(key=api_key,output_format="pandas")
data,meta_data=time_series.get_daily(symbol="MSFT",outputsize="full")
data=data.rename(columns={
            '1.open' : 'Open',
            '2.high' : 'High',
            '3.low' : 'Low',
            '4.close' : 'Close',
            '5.volume' : 'Volume',
                         })
data['Open-Close'] = (data.Open - data.Close)/data.Open
data['High-Low'] = (data.High - data.Low)/data.Low
data['percent_change'] = data['close'].pct_change()
data['std_5']=data['percent_change'].rolling(5).std()
data['ret_5']=data['percent_change'].rolling(5).mean()
data.dropna(inplace=TRUE)









