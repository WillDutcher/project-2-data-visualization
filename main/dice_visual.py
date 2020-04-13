from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two d6 dice.
die1 = int(input("How many sides does die 1 have? "))
die2 = int(input("How many sides does die 2 have? "))
die_1 = Die(die1)
die_2 = Die(die2)

# Make some rolls and store results in a list.
results = []
num_times = int(input("How many times do you want to roll? "))
for roll_num in range(1, num_times + 1):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling two dice (d{die1} and d{die2}) \
    {num_times} times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
    filename=f'd{die1}d{die2}_{num_times}_times.html')

print(frequencies)
