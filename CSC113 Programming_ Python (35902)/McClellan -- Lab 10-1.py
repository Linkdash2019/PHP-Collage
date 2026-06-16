#Cameron McClellan
#Lab: Data Visualization - Generating Data
from cProfile import label

import matplotlib.pyplot as plot
from random import randint
import plotly.express as px
from matplotlib.pyplot import title


#Exersise 15-1 and 2
def graph():
    fig, ax = plot.subplots()
    # Graph settings--------------------------------------
    ax.plot(values, squares, linewidth=1)
    ax.set_title("Cubed Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)
    ax.tick_params(labelsize=14)
    ax.ticklabel_format(style='plain')
    ax.scatter(range(1, counter), squares, c=squares,  s = 50)
    # ----------------------------------------------------
    plot.show()

#5 graph
counter = 1
squares = []
values = []

for x in range(5):
    squares.append(counter*counter*counter)
    values.append(x+1)
    counter += 1
graph()

#5000 graph
counter = 1
squares = []
values = []

for x in range(5000):
    squares.append(counter*counter*counter)
    values.append(x+1)
    counter += 1
graph()

#Exersise 15-6
class Die:
    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die = Die()
results1 = []
results2 = []
for roll_num in range(9999999):
    result1 = die.roll()
    results1.append(result1)

    result2 = die.roll()
    results2.append(result2)

#print(results1)
#print(results2)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results1.count(value)+results2.count((value))
    frequencies.append(frequency)
#print(frequencies)

title = "2 D8 dice rolled 1,000 times"
labels = {'x': 'Results', 'y': 'Frequency'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()