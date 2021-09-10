from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
label=['Player 1', 'Player2', 'Player3']
colors = ['#6d904f','#fc4f30','#008fd5']

plt.stackplot(minutes, player1, player2, player3, labels=label, colors=colors)
plt.legend(loc = 'upper left') # We can hardcode the location of the legend by loc parameter
# plt.legend(loc = (0.07 , 0.05)) # Or we can pass a tuple, 7% right and 5% above the axes respectively

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f