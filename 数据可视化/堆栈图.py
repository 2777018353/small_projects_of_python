#  stackplot
import matplotlib.pyplot as plt 

month = [1,2,3,4,5,6,7,8,9,10,11,12]

A = [1,2,3,4,5,6,7,8,9,10,11,12]
B = [10,20,30,40,50,60,70,80,90,100,110,120]
C = [200,190,180,170,160,150,140,130,120,110,100,90]
D = [50,40,50,60,50,56,57,58,59,60,59,60]

plt.plot([], [], color='m', label='Company A', linewidth=8)
plt.plot([], [], color='c', label='Company B', linewidth=8)
plt.plot([], [], color='r', label='Company C', linewidth=8)
plt.plot([], [], color='k', label='Company D', linewidth=8)

plt.stackplot(month, A, B, C, D, colors=['m','c','r','k'])
plt.xlabel('month')
plt.ylabel('sales')
plt.title('A B C D sales')
plt.legend()

plt.show()