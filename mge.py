from global_constants import CONST


def get_a11(DFIXYZ, DET):
    a = [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["localNodes"])]

    # оскільки гауса і c-шки однаково генеряться по розмірах то можна просто форік по 27

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

                a[i][j] += consts * \
                           (CONST["lambda"] * (1 - CONST["nu"]) * dx +
                            CONST["mu"] * (dy + dz)) * \
                           DET[node]
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

                a[i][j] += consts * \
                           (CONST["lambda"] * (1 - CONST["nu"]) * dy +
                            CONST["mu"] * (dx + dz)) * \
                           DET[node]
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

                a[i][j] += consts * \
                           (CONST["lambda"] * (1 - CONST["nu"]) * dz +
                            CONST["mu"] * (dx + dy)) * \
                           DET[node]
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

                a[i][j] += consts * \
                           (CONST["lambda"] * CONST["nu"] * dxdy +
                            CONST["mu"] * dydx) * \
                           DET[node]
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

                a[i][j] += consts * \
                           (CONST["lambda"] * CONST["nu"] * dxdz +
                            CONST["mu"] * dzdx) * \
                           DET[node]
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

                a[i][j] += consts * \
                           (CONST["lambda"] * CONST["nu"] * dydz +
                            CONST["mu"] * dzdy) * \
                           DET[node]
    return a


def get_MGE(a11, a12, a13, a22, a23, a33):
    mge = [[0 for _ in range(CONST["mgeSize"])]
           for _ in range(CONST["mgeSize"])]

    for i in range(CONST["localNodes"]):
        for j in range(CONST["localNodes"]):
            # diagonals
            mge[i][j] = a11[i][j]
            mge[i + 20][j + 20] = a22[i][j]
            mge[i + 40][j + 40] = a33[i][j]

            mge[i][j + 20] = a12[i][j]
            mge[i][j + 40] = a13[i][j]
            mge[i + 20][j + 40] = a23[i][j]

    return mge
