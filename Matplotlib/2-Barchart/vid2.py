import csv
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter # This makes keeping track of frequency in dictionary easier
import numpy as np

plt.style.use("fivethirtyeight")

###### USING CSV MODULE ######
# with open('Vid-2\data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file) # Parses the file in the form of key-value pairs

#     language_counter = Counter() # Initialize counter
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';')) # Adds the languages which are seperated by semicolon


###### USING PANDAS ######
language_counter = Counter()
data = pd.read_csv('Vid-2\data.csv')
ids = data['Responder_id']
lang_response = data['LanguagesWorkedWith']

for response in lang_response:
    language_counter.update(response.split(';'))


languages = []
popularity = []

for item in language_counter.most_common(15): # most_common method returns a list of tuples of the top frequency languages
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
# reverses the list so that the most popular language is at the top            

plt.barh(languages , popularity)

    # row = next(csv_reader) # Stores the first row only

# print(row)
# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexes = np.arange(len(ages_x)) # Creates a numpy array starting from 0 to the length
# width = 0.25 # Declaring a custom width of the chart
# # plt.plot(x,y) makes a default line chart
# # plt.bar(x,y) makes a bar chart
# plt.barh(x,y) makes a horizontal bar chart



# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_indexes - width, dev_y, width=width , color="#444444", label="All Devs")
# # width paramter sets the customised width of the graph

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width , color="#008fd5", label="Python")

# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_indexes + width,  js_dev_y, width=width ,color="#e5ae38", label="JavaScript")

# plt.legend()

# plt.xticks(ticks=x_indexes , labels=ages_x)
# # Changes the x labels from (0,10) to actual age values

plt.title("Most popular programming languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.show()