import numpy as np
import matplotlib as plt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
from sklearn.ensemble import RandomForestClassifier
api_key="MNNSPRF08WG4DTL3"
time_key = TimeSeries(key=api_key,output_format="pandas")
data,meta_data=time_series.get_daily(symbol="MSFT",outputsize="full")

