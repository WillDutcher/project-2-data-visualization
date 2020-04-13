"""
A number raised to the third power is a cube.
Plot the first five cubic numbers and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

# First 5000
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-deep')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='#33F0D7', s=1)

# Set chart title and label axes
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value')
ax.set_ylabel('Cube of Value')

# Set range for each axis.
ax.axis([0, 5001, 0, 126000000000])

# Set the size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('cubes_2_plot.png', bbox_inches='tight')
plt.show() # Show on-screen
