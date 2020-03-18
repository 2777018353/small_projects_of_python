import matplotlib.pyplot as plt 
import numpy as np 

x, y = np.loadtxt('数据可视化\example.csv', delimiter=',', unpack=True)

plt.plot(x, y, label='Data loaded from csv file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('I have loaded a csv file, amazing! Wow~')
plt.legend()

plt.show()
