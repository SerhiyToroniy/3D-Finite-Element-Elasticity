import matplotlib.pyplot as plt


def display_3d_grid(coords):
    # Separate the x, y, and z coordinates
    x, y, z = zip(*coords)

    # Create a figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(x, y, z)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'3D Grid of Points ({len(coords)})')

    # Adjust the view angle
    ax.view_init(elev=30, azim=-45)

    # Show the plot
    plt.show()
