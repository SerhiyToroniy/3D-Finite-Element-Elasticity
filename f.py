import numpy as np


def get_F(FE_list, AKT_COUNT, NT):
    F = np.zeros((3 * AKT_COUNT)).tolist()
    for fe in FE_list:
        index_of_FE = FE_list.index(fe)
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
            index_i_for_F = 3 * NT[index_of_FE][i_for_NT] + xyz_cord_i
            F[index_i_for_F] += fe[i]
    return F
