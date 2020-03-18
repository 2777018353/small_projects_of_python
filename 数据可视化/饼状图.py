import matplotlib.pyplot as plt 

sales = [1,8,3.5,7.8]
company_names = ['company A', 'company B', 'company C', 'company D']
color = ['azure', 'lavender', 'pink', 'aqua']

plt.pie(sales, labels=company_names, colors=color, startangle=90, shadow=True, autopct='%1.1f%%', explode=(0.1,0,0,0))

plt.show()
