import matplotlib.pyplot as plt 

x = [1, 3, 5]
y = [1, 2, 3]

x2 = [2, 4, 6]
y2 = [3, 2, 1]

plt.bar(x, y, label='Bar_1', color='blue')
plt.bar(x2, y2, label='Bar_2', color='c')

plt.xlabel('Company name')
plt.ylabel('2019 Sales')
plt.title('ABC Compare')
plt.legend()

plt.show()