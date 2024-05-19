import numpy as np


def get_F(FE, AKT_COUNT, NT):
    big_matrix = np.zeros((3 * AKT_COUNT))
    result = big_matrix.tolist()
    for fe in FE:
        index_of_FE = FE.index(fe)
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

            index_i_for_FE = 3 * NT[index_of_FE][i_for_NT] + xyz_cord_i
            result[index_i_for_FE] += fe[i]
    return result
