import numpy as np

from global_constants import CONST


def get_ZU(AKT, NT):
    zu = []
    for side in CONST["ZU"]:
        local_coords = NT[side["element"]]
        surface_indexes = []
        if side["nodes"] == "all":
            surface_indexes = CONST["sideNTindexes"][side["side"]]
        else:
            for side_node in side["nodes"]:
                surface_indexes.append(side_node)
        zu.append([AKT[local_coords[i]].coords for i in surface_indexes])

    return zu


def remove_duplicates_ZU(ZU):
    converted_ZU = []
    for row in ZU:
        for point in row:
            converted_ZU.append(point)
    unique_points = set(tuple(point) for point in converted_ZU)
    unique_points_list = [list(point) for point in unique_points]
    points = np.array(unique_points_list)
    sorted_points = points[np.lexsort((points[:, 0], points[:, 1], points[:, 2]))].tolist()  # sorting by z then by y then by x

    return sorted_points
