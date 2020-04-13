"""
A number raised to the third power is a cube.
Plot the first five cubic numbers and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

# First 5
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('fast')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='#11BB3C', s=50)

# Set chart title and label axes
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

# Set range for each axis.
ax.axis([0, 6, 0, 130])

# Set the size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()
