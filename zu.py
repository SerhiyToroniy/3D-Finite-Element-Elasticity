import numpy as np

from global_constants import CONST


def get_ZU(AKT, NT):
    zu = []
    for side in CONST["ZU"]:
        local_coords = NT[side["element"]]
        surface_indexes = CONST["sideNTindexes"][side["side"]]
        zu.append([AKT[local_coords[i]].coords for i in surface_indexes])

    return zu


def convert_ZU_to_layer(ZU):
    converted_ZU = []
    for row in ZU:
        for point in row:
            converted_ZU.append(point)
    unique_points = set(tuple(point) for point in converted_ZU)
    unique_points_list = [list(point) for point in unique_points]
    points = np.array(unique_points_list)
    sorted_points = points[np.lexsort((points[:, 0], points[:, 1], points[:, 2]))].tolist()

    return sorted_points

