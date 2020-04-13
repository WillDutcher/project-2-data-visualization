import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.style.use('seaborn-talk')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)


# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
