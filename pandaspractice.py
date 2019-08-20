import pandas as pd
import matplotlib.pyplot as plt

symbols = ['SPY', 'GOOG', 'IBM', 'GLD']
start_date = '2010-01-01'
end_date = '2010-12-31'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)


for symbol in symbols:
    df_tmp = pd.read_csv("data\{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=[
        'Date', 'Adj Close'], na_values=['nan'])
    df_tmp = df_tmp.rename(columns={'Adj Close': symbol})
    df1 = df1.join(df_tmp)


df1 = df1.dropna()
print(df1.ix['2010-01-01':'2010-01-10'], ['GOOG'])


ax = df1.plot(title='Stock prices')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.show()
'''



'''
