import plotly.graph_objects as go

from global_constants import CONST


def plot_line(fig, start_point, end_point, color='blue', width=1):
    x_start, y_start, z_start = start_point
    x_end, y_end, z_end = end_point
    fig.add_trace(go.Scatter3d(x=[x_start, x_end], y=[y_start, y_end], z=[z_start, z_end],
                               mode='lines',
                               line=dict(color=color, width=width)))


def plot_point(fig, point, color='blue', size=5, text=None):
    x, y, z = point
    fig.add_trace(go.Scatter3d(
        x=[x], y=[y], z=[z],
        mode='markers+text' if text else 'markers',
        marker=dict(size=size, color=color),
        text=[text] if text else None
    ))


def plot_zu(fig, zu):
    zu_line_width = 5
    for side in zu:
        if len(side) == 8:
            plot_line(fig, side[0], side[1], 'red', zu_line_width)
            plot_line(fig, side[1], side[2], 'red', zu_line_width)
            plot_line(fig, side[2], side[3], 'red', zu_line_width)
            plot_line(fig, side[3], side[0], 'red', zu_line_width)
        for point in side:
            plot_point(fig, point, 'red', zu_line_width)


def plot_zp(fig, zp):
    zp_line_width = 5
    for side in zp:
        for point in side:
            plot_point(fig, point, 'green', zp_line_width)

        plot_line(fig, side[0], side[4], 'green', zp_line_width)
        plot_line(fig, side[4], side[1], 'green', zp_line_width)

        plot_line(fig, side[1], side[5], 'green', zp_line_width)
        plot_line(fig, side[5], side[2], 'green', zp_line_width)

        plot_line(fig, side[2], side[6], 'green', zp_line_width)
        plot_line(fig, side[6], side[3], 'green', zp_line_width)

        plot_line(fig, side[3], side[7], 'green', zp_line_width)
        plot_line(fig, side[7], side[0], 'green', zp_line_width)


def display_3d_grid(coords, nt, zu, zp):
    x, y, z = zip(*coords)
    enumarted_AKT = list(zip(x, y, z))

    fig = go.Figure()

    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers+text',
                               marker=dict(size=5), text=[str(i + 1) for i in range(len(coords))]))

    # Plot lines for each element
    for element in nt:
        # lower layer
        plot_line(fig, enumarted_AKT[element[0]], enumarted_AKT[element[8]])
        plot_line(fig, enumarted_AKT[element[8]], enumarted_AKT[element[1]])

        plot_line(fig, enumarted_AKT[element[1]], enumarted_AKT[element[9]])
        plot_line(fig, enumarted_AKT[element[9]], enumarted_AKT[element[2]])

        plot_line(fig, enumarted_AKT[element[2]], enumarted_AKT[element[10]])
        plot_line(fig, enumarted_AKT[element[10]], enumarted_AKT[element[3]])

        plot_line(fig, enumarted_AKT[element[3]], enumarted_AKT[element[11]])
        plot_line(fig, enumarted_AKT[element[11]], enumarted_AKT[element[0]])

        # upper layer
        plot_line(fig, enumarted_AKT[element[4]], enumarted_AKT[element[16]])
        plot_line(fig, enumarted_AKT[element[16]], enumarted_AKT[element[5]])

        plot_line(fig, enumarted_AKT[element[5]], enumarted_AKT[element[17]])
        plot_line(fig, enumarted_AKT[element[17]], enumarted_AKT[element[6]])

        plot_line(fig, enumarted_AKT[element[6]], enumarted_AKT[element[18]])
        plot_line(fig, enumarted_AKT[element[18]], enumarted_AKT[element[7]])

        plot_line(fig, enumarted_AKT[element[7]], enumarted_AKT[element[19]])
        plot_line(fig, enumarted_AKT[element[19]], enumarted_AKT[element[4]])

        # between layers
        plot_line(fig, enumarted_AKT[element[0]], enumarted_AKT[element[12]])
        plot_line(fig, enumarted_AKT[element[12]], enumarted_AKT[element[4]])

        plot_line(fig, enumarted_AKT[element[1]], enumarted_AKT[element[13]])
        plot_line(fig, enumarted_AKT[element[13]], enumarted_AKT[element[5]])

        plot_line(fig, enumarted_AKT[element[2]], enumarted_AKT[element[14]])
        plot_line(fig, enumarted_AKT[element[14]], enumarted_AKT[element[6]])

        plot_line(fig, enumarted_AKT[element[3]], enumarted_AKT[element[15]])
        plot_line(fig, enumarted_AKT[element[15]], enumarted_AKT[element[7]])

    # Plot ZU elements
    plot_zu(fig, zu)

    # Plot ZP elements
    plot_zp(fig, zp)

    # Update layout
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectratio=dict(x=CONST["size"]["x"], y=CONST["size"]["y"], z=CONST["size"]["z"])
    ),
        title=f'AKT ({len(coords)} nodes)',
        scene_camera=dict(
            eye=dict(x=3, y=-4, z=3),
        )
    )

    fig.show()
