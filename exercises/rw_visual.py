import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as program is active.
while True:
    # Make a random walk.
    try:
        how_far = int(input("How many steps do you want to walk? "))
        print(f"You walked {str(how_far)} steps.")
    except ValueError:
        print("You're walking 5,000 steps.")
        how_far = 5000
    rw = RandomWalk(how_far)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fix, ax = plt.subplots()

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)

    # Show the path walked.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Show the title.
    ax.set_title('Random Path Walked')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # plt.savefig('rw_visual_sample.png', bbox_inches='tight')
    plt.show()

    walk_again = input("Would you like to take another random walk? (y/n): ")
    if walk_again.lower() == 'n':
        break
