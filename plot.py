import matplotlib.pyplot as plt
import numpy as np

from global_constants import CONST


def plot_line(ax, start_point, end_point, color='green'):
    x_start, y_start, z_start = start_point
    x_end, y_end, z_end = end_point
    ax.plot([x_start, x_end], [y_start, y_end], [z_start, z_end], color=color)


def plot_zu(ax, zu):
    for side in zu:
        plot_line(ax, side[0], side[1], 'red')
        plot_line(ax, side[1], side[2], 'red')
        plot_line(ax, side[2], side[3], 'red')
        plot_line(ax, side[3], side[0], 'red')

        # create X
        # plot_line(ax, side[0], side[2], 'red')
        # plot_line(ax, side[1], side[3], 'red')


def display_3d_grid(coords, nt, zu):
    x, y, z = zip(*coords)
    enumarted_AKT = list(zip(x, y, z))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)

    for element in nt:
        # lower layer
        plot_line(ax, enumarted_AKT[element[0]], enumarted_AKT[element[1]])
        plot_line(ax, enumarted_AKT[element[1]], enumarted_AKT[element[2]])
        plot_line(ax, enumarted_AKT[element[2]], enumarted_AKT[element[3]])
        plot_line(ax, enumarted_AKT[element[3]], enumarted_AKT[element[0]])

        # upper layer
        plot_line(ax, enumarted_AKT[element[4]], enumarted_AKT[element[5]])
        plot_line(ax, enumarted_AKT[element[5]], enumarted_AKT[element[6]])
        plot_line(ax, enumarted_AKT[element[6]], enumarted_AKT[element[7]])
        plot_line(ax, enumarted_AKT[element[7]], enumarted_AKT[element[4]])

        # between layers
        plot_line(ax, enumarted_AKT[element[0]], enumarted_AKT[element[4]])
        plot_line(ax, enumarted_AKT[element[1]], enumarted_AKT[element[5]])
        plot_line(ax, enumarted_AKT[element[2]], enumarted_AKT[element[6]])
        plot_line(ax, enumarted_AKT[element[3]], enumarted_AKT[element[7]])

    plot_zu(ax, zu)

    for i, (px, py, pz) in enumerate(zip(x, y, z)):
        ax.text(px, py, pz, f'{i + 1}', color='blue', fontsize=8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'AKT ({len(coords)} nodes)')

    ax.set_box_aspect([CONST["size"]["x"], CONST["size"]["y"], CONST["size"]["z"]])

    plt.show()
