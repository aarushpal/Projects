import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

###### BASIC #######
# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# bins = [10,20,30,40,50,60]
# plt.hist(ages , bins=bins , edgecolor = 'black')
# # edgecolor - helps in demarcating different bins
# # bins - basically bargraphs that the plot will divide our data into


data = pd.read_csv('Task-2/6-Histograms\data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [20,30,40,50,60,70,80,90,100]

plt.hist(ages , bins=bins , edgecolor = 'black' , log=True)
# log - converts the plot to logarithmic scale(for better visulization)

median_age = 29
color = '#fc4f30'
plt.axvline(median_age , color=color , label= 'Median Age' , linewidth = 2)
# axvline - axis vertical line

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()