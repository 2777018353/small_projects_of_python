import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [6,5,7,4,8,6,5,4,6,6,7,10]

x2 = [1,2,3,4,5,6,7,8,9,10,11,12]
y2 = [5,6,9,1,8,5,0,9,5,2,9,2]

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title("Sales of Company\nCompany A and Company B")

plt.plot(x, y, label='Company A')
plt.plot(x2, y2, label='Company B')
plt.legend()
plt.show()