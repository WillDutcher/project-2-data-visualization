import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100) # s = size of the scatter plot dot
# ax.scatter(x_values, y_values, c='#EE346F', s=10) # s = size of the scatter plot dot

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set the size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show() # Show on-screen
plt.savefig('squares_plot.png', bbox_inches='tight')