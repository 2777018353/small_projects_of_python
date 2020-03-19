import pandas as pd 

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

user_input_cols = ['000','shape','first_name','c','d','e','f','g','h']

df = pd.read_csv('numpy和pandas介绍\\diabetes.csv',
                index_col=False,  #  '0' means cancel the Rank, you can choose which one as the first colums
                header=None,
                names=user_input_cols
                )

print(df['000'].head())
print(df.c)  #  print(df.000) or print(df.first_name) error!

new_series = df.c + ',' + df.d
df['series + series'] = new_series
print(df.head())
df = pd.read_csv('numpy和pandas介绍\\diabetes.csv')
print(df.describe())
print(df.dtypes)