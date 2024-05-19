from global_constants import CONST
import numpy as np


def get_a11(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dx = DFIXYZ[node][i][0] * DFIXYZ[node][j][0]
                dy = DFIXYZ[node][i][1] * DFIXYZ[node][j][1]
                dz = DFIXYZ[node][i][2] * DFIXYZ[node][j][2]

                a[i][j] += consts * (CONST["lambda"] * (1 - CONST["nu"]) * dx + CONST["mu"] * (dy + dz)) * DET[node]
    return a


def get_a22(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dx = DFIXYZ[node][i][0] * DFIXYZ[node][j][0]
                dy = DFIXYZ[node][i][1] * DFIXYZ[node][j][1]
                dz = DFIXYZ[node][i][2] * DFIXYZ[node][j][2]

                a[i][j] += consts * (CONST["lambda"] * (1 - CONST["nu"]) * dy + CONST["mu"] * (dx + dz)) * DET[node]
    return a


def get_a33(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dx = DFIXYZ[node][i][0] * DFIXYZ[node][j][0]
                dy = DFIXYZ[node][i][1] * DFIXYZ[node][j][1]
                dz = DFIXYZ[node][i][2] * DFIXYZ[node][j][2]

                a[i][j] += consts * (CONST["lambda"] * (1 - CONST["nu"]) * dz + CONST["mu"] * (dx + dy)) * DET[node]
    return a


def get_a12(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dxdy = DFIXYZ[node][i][0] * DFIXYZ[node][j][1]
                dydx = DFIXYZ[node][i][1] * DFIXYZ[node][j][0]

                a[i][j] += consts * (CONST["lambda"] * CONST["nu"] * dxdy + CONST["mu"] * dydx) * DET[node]
    return a


def get_a13(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dxdz = DFIXYZ[node][i][0] * DFIXYZ[node][j][2]
                dzdx = DFIXYZ[node][i][2] * DFIXYZ[node][j][0]

                a[i][j] += consts * (CONST["lambda"] * CONST["nu"] * dxdz + CONST["mu"] * dzdx) * DET[node]
    return a


def get_a23(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            for node in range(CONST["gaussianNodes_3D"]):
                consts = \
                    CONST["gaussianConsts_3D"][node][0] * \
                    CONST["gaussianConsts_3D"][node][1] * \
                    CONST["gaussianConsts_3D"][node][2]

                dydz = DFIXYZ[node][i][1] * DFIXYZ[node][j][2]
                dzdy = DFIXYZ[node][i][2] * DFIXYZ[node][j][1]

                a[i][j] += consts * (CONST["lambda"] * CONST["nu"] * dydz + CONST["mu"] * dzdy) * DET[node]
    return a


def get_MGE(a11, a12, a13, a22, a23, a33):
    mge = np.zeros((CONST["mgeSize"], CONST["mgeSize"]))

    matrix_a11 = np.array(a11)
    matrix_a12 = np.array(a12)
    matrix_a13 = np.array(a13)
    matrix_a22 = np.array(a22)
    matrix_a23 = np.array(a23)
    matrix_a33 = np.array(a33)

    mge[:20, :20] = matrix_a11
    mge[:20, 20:40] = matrix_a12
    mge[:20, 40:] = matrix_a13
    mge[20:40, :20] = matrix_a12.T
    mge[20:40, 20:40] = matrix_a22
    mge[20:40, 40:] = matrix_a23
    mge[40:, :20] = matrix_a13.T
    mge[40:, 20:40] = matrix_a23.T
    mge[40:, 40:] = matrix_a33

    mge = mge.tolist()

    return mge
