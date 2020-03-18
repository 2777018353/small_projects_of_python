import matplotlib.pyplot as plt 

City_A_Age = [1,2,5,7,9,10,13,14,15,18,19,20,21,25,24,28,29,24,27,30,36,34,373,937,40,46,48,47,50,54,58,60,67,64,70,89,60,90,100]
bins = [0,10,20,30,40,50,60,70,80,90,100,110]

plt.hist(City_A_Age, bins,histtype='bar', rwidth=0.8)
plt.xlabel('Age')
plt.ylabel('Num')
plt.title('The city A Age Hist')
plt.show()
