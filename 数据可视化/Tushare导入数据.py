import tushare as ts 

#  df = ts.get_hist_data('000001', start='2019-01-01', end='2020-01-01').reset_index().sort_values('date')
df = ts.get_hist_data('000001', start='2019-01-01', end='2020-01-01').sort_index(ascending=True)

df.low.plot()