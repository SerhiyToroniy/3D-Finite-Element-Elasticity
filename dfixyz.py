from global_constants import CONST
from scipy.linalg import solve


def get_DFIXYZ(DJ, DFIABG):
    DFIXYZ_list = [
        [0 for _ in range(CONST["localNodes"])]
        for _ in range(CONST["gaussianNodes_3D"])]

    for gaussNode in range(CONST["gaussianNodes_3D"]):
        for localIndex in range(CONST["localNodes"]):
            DFIXYZ_list[gaussNode][localIndex] = solve(
                DJ[gaussNode],
                [DFIABG[gaussNode][0][localIndex],
                 DFIABG[gaussNode][1][localIndex],
                 DFIABG[gaussNode][2][localIndex]]).tolist()

    return DFIXYZ_list
