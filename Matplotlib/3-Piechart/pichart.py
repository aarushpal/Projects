  
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

####### COLORS AND LABELS #######
# slices = [120 , 80 , 30 , 20]
# labels = ['Sixty' ,  'Forty' , 'Extra1' , 'Extra2']
# colors = ['#008fd5' , '#fc4f30' , '#e5ae37' , '#6d904f']
# plt.pie(slices , labels=labels , colors=colors ,  wedgeprops={'edgecolor' : 'black'})
# labels - gives names to the slices
# wedgeprops edgecolor - gives a boundary that demarcates different pie regions


###### NOTE #######
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# we usually use pie chart to plot less number of items because, otherwise it looks crowded


####### EXPLODE , SHADOW , STARTANGLE , AUTOPCT #######
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0 , 0 , 0 , 0.1 , 0]
# explode - offsets a region outside to sort of highlight it
# 0.1 represents that the Python region will come out 10% of the radius of the pie chart
# shadow gives a shadow(duh), a more 3d look
# start angle rotates the chart by the given angle anticlockwise
# autopct displays the percentage of the chart , a particular region occupies

plt.pie(slices , labels=labels , explode=explode , shadow=True , startangle=90 , autopct='%1.1f%%' ,wedgeprops={'edgecolor' : 'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f