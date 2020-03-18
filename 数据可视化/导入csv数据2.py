import matplotlib.pyplot as plt 
import pandas as pd 

data1 = pd.read_csv('数据可视化\example.csv')

type(data1)

number = data1.column_b.iloc[8]
print(number)