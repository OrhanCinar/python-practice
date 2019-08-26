import pandas as pd
import matplotlib.pyplot as plt

symbols = ['SPY']
start_date = '2010-01-01'
end_date = '2010-12-31'
dates = pd.date_range(start_date, end_date)

df = pd.read_csv("data\\SPY.csv", index_col='Date',
                 parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

mean = df.mean()

df.hist(bins=50)
#  plt.axvline(mean)
plt.show()
