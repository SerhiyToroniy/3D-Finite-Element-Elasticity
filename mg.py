import numpy as np

from node import Node


def get_MG(MGE, NT, ZU, AKT):
    nodes_count = len([_ for _ in AKT])
    big_matrix = np.zeros((3 * nodes_count, 3 * nodes_count))
    result = big_matrix.tolist()

    for mge in MGE:
        index_of_MGE = MGE.index(mge)
        for j in range(60):
            for i in range(60):

                if i < 20:
                    xyz_cord_i = 0
                    i_for_NT = i
                elif 19 < i < 40:
                    xyz_cord_i = 1
                    i_for_NT = i - 20
                else:
                    xyz_cord_i = 2
                    i_for_NT = i - 40

                if j < 20:
                    xyz_cord_j = 0
                    j_for_NT = j
                elif 19 < j < 40:
                    xyz_cord_j = 1
                    j_for_NT = j - 20
                else:
                    xyz_cord_j = 2
                    j_for_NT = j - 40

                index_i_for_MG = 3 * NT[index_of_MGE][i_for_NT] + xyz_cord_i
                index_j_for_MG = 3 * NT[index_of_MGE][j_for_NT] + xyz_cord_j
                result[index_j_for_MG][index_i_for_MG] += mge[j][i]

    for i in ZU:
        target_node = Node(i)
        index_of_point = -1
        index_counter = 0
        for node in AKT:
            if node.coords[0] == target_node.coords[0] \
                    and node.coords[1] == target_node.coords[1] \
                    and node.coords[2] == target_node.coords[2]:
                index_of_point = index_counter
                break
            index_counter += 1
        ix = 3 * index_of_point + 0
        iy = 3 * index_of_point + 1
        iz = 3 * index_of_point + 2
        result[ix][ix] = 10000000000000000
        result[iy][iy] = 10000000000000000
        result[iz][iz] = 10000000000000000

    return result