from node import *


def get_AKT_modified(AKT, U):  # U = F = 3 * AKT
    for index_U in range(0, len(U), 3):
        index_AKT = index_U // 3
        new_coords = AKT[index_AKT].coords
        new_coords[0] += U[index_U]
        new_coords[1] += U[index_U + 1]
        new_coords[2] += U[index_U + 2]
        AKT[index_AKT] = Node(coords=new_coords)

    return AKT
