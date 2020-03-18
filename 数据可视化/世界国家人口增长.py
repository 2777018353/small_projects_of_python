from matplotlib import pyplot as plt 
import pandas as pd 

data = pd.read_csv('数据可视化\countries.csv')

China_filter = data.country == 'China'  #  成立为True, 否则为False
China_data = data[China_filter]  #  筛选出True的元素

US_filter = data.country == 'United States'
US_data = data[US_filter]

JP_filter = data.country == 'Japan'
JP_data = data[JP_filter]

plt.plot(China_data.year, China_data.population / China_data.population.iloc[0])
plt.plot(US_data.year, US_data.population / US_data.population.iloc[0])
plt.plot(JP_data.year, JP_data.population / JP_data.population.iloc[0])

plt.title('Country Population')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend(['China', 'US', 'JP'])

plt.show()
