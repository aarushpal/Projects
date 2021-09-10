import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('Task-2/5-Fill_Betweens\data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

overall_median = 57287

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')
plt.fill_between(ages , py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha = 0.5, label='Above avg')
# default y2 (threshold) is 0 , but we can pass it as the third argument
# alpha denotes the degree of transparency

plt.fill_between(ages , py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, alpha = 0.5, label='Below avg')



plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()