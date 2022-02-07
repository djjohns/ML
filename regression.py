import pandas as pd
import quandl as qu
import math

# Grab our base dataset from quandl.
df = qu.get('WIKI/GOOGL')
# Refine to what you want to look at.
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
# High Low percentage.
df['HL_Percent']  = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# Daily precent change.
df['PCT_change']  = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# Drop down to what we want to look at.
df = df[['Adj. Close', 'HL_Percent', 'PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) # Treat NaNs as an outliers.

# Regression algorithm
# Use a percentage of the df to forecast next 10 days.
# math.ceil() will round up to nearest whole number.
# Convert the float to an int.
forecast_out = int(math.ceil(0.01*len(df)))
# Label column for each row will be adjusted close price 10 days into the future.
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())