#scatter
import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,1,5,3,7,9,8,7,10]

plt.scatter(x, y, label='scatter_plot', marker='*', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title('A scatter plot')
plt.legend()

plt.show()
