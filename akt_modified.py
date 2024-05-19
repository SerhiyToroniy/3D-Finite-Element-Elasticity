import numpy as np
from node import *


def get_AKT_modified(AKT, u):  # u = f = 3 * AKT
    oldCoords_x = [node.coords[0] for node in AKT]
    oldCoords_y = [node.coords[1] for node in AKT]
    oldCoords_z = [node.coords[2] for node in AKT]

    newCoords_x = [0] * len(AKT)
    newCoords_y = [0] * len(AKT)
    newCoords_z = [0] * len(AKT)

    for i in range(0, len(u), 3):
        j = i // 3
        newCoords_x[j] = oldCoords_x[j] + u[i]
        newCoords_y[j] = oldCoords_y[j] + u[i + 1]
        newCoords_z[j] = oldCoords_z[j] + u[i + 2]

    new_AKT = []

    for i in range(len(AKT)):
        new_AKT.append(Node(coords=[newCoords_x[i],
                                    newCoords_y[i],
                                    newCoords_z[i]]))

    return new_AKT
