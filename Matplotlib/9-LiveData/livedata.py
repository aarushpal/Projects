import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


###### BASIC #######
# x_vals = []
# y_vals = []

# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))
#     plt.cla() # cla - clear axis, removes the previous plot and redraws the new plot with the same colour
#     plt.plot(x_vals, y_vals)

# ani = FuncAnimation(plt.gcf() , animate , interval=1000) 
# # 1st param - takes the object to animate
# # 2nd param - takes a function to iterate through
# # 3rd param - interval denotes the time period in milliseconds
# plt.tight_layout()
# plt.show()


def animate(i):
    data = pd.read_csv('Task-2\9-LiveData\data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1 , label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf() , animate , interval=1000) 
plt.show()

