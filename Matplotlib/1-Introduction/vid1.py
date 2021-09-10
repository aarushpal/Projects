from matplotlib import pyplot as plt

# print(plt.style.available) # Prints the available styling options

# plt.style.use('fivethirtyeight') # Using the available style
# plt.xkcd() # Gives a comic book like design

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x , dev_y , color='k', linestyle='--', marker='.', linewidth = '3', label = 'All devs') 
# 1st parameter takes the x axis value and 2nd one takes y axis value
# Creates plot but does not display it
# We can also pass hex values for the color
# format string takes the parameters as [marker][line][colour]
# Default linewidth is 1 but we can pass it as an argument to widen the line

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x , py_dev_y , color='b', linestyle='--', marker='o', label = 'Python devs' )

plt.xlabel('Ages') # Labels the x axis
plt.ylabel('Median Salary') # Labels the y axis
plt.title('Median Salary by Age') # Gives title to the plot
plt.legend()

### plt.legend(['All devs', 'Python devs']) # Labels the lines according to the order in which they are plotted

plt.tight_layout() # Fixes the padding

plt.savefig('plot.png') # Saves the plot image as png file in the current directory
# We can also pass in the path of other directories 
plt.show() # Actually displays the plot
