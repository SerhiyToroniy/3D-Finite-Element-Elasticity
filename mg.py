import numpy as np


def get_MG(MGE, NT, ZU, AKT):
    nodes_count = len([_ for _ in AKT])
    big_matrix = np.zeros((3 * nodes_count, 3 * nodes_count))
    result = big_matrix.tolist()

    for mge in MGE:
        index_of_MGE = MGE.index(mge)
        for i in range(60):
            for j in range(60):

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
                result[index_i_for_MG][index_j_for_MG] += mge[i][j]

    for i in ZU:
        akt_list = [node.coords for node in AKT]
        global_index_of_point = akt_list.index(i)
        ix = 3 * global_index_of_point + 0
        iy = 3 * global_index_of_point + 1
        iz = 3 * global_index_of_point + 2
        result[ix][ix] = float('inf')
        result[iy][iy] = float('inf')
        result[iz][iz] = float('inf')

    return result
