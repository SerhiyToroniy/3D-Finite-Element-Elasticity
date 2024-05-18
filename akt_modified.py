import numpy as np
from node import *


def get_AKT_modified(AKT, deltaCoords):
    oldCoords_x = [node.coords[0] for node in AKT]
    oldCoords_y = [node.coords[1] for node in AKT]
    oldCoords_z = [node.coords[2] for node in AKT]

    newCoords_x = np.zeros(len(AKT)).tolist()
    newCoords_y = np.zeros(len(AKT)).tolist()
    newCoords_z = np.zeros(len(AKT)).tolist()

    new_AKT = []

    for i in range(len(deltaCoords)):
        j = i // 3
        if (i + 1) % 3 == 1:
            newCoords_x[j] = oldCoords_x[j] + deltaCoords[i]
            j += 1
        if (i + 1) % 3 == 2:
            newCoords_y[j] = oldCoords_y[j] + deltaCoords[i]
            j += 1
        if (i + 1) % 3 == 0:
            newCoords_z[j] = oldCoords_z[j] + deltaCoords[i]
            j += 1

    for i in range(len(AKT)):
        new_AKT.append(Node(coords=[newCoords_x[i],
                                    newCoords_y[i],
                                    newCoords_z[i]]))

    return new_AKT
