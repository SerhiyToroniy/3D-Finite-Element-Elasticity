from math import sqrt

CONST = {}

CONST["axes"] = 3
CONST["size"] = {"x": 2, "y": 2, "z": 2}
CONST["division"] = {"x": 2, "y": 2, "z": 2}

CONST["elementsNumber"] = CONST["division"]["x"] * CONST["division"]["y"] * CONST["division"]["z"]

CONST["localNodes"] = 20

CONST["ZU"] = [
    {"element": 0, "side": 5},
    {"element": 1, "side": 5},
    {"element": 2, "side": 5},
    {"element": 3, "side": 5},
]

CONST["ZP"] = [
    {"element": 4, "side": 6},
    # {"element": 5, "side": 6},
    # {"element": 6, "side": 6},
    # {"element": 7, "side": 6},
]

CONST["sideNTindexes"] = {
    1: [1, 2, 6, 5, 9, 14, 17, 13],
    2: [0, 1, 5, 4, 8, 13, 16, 12],
    3: [0, 3, 7, 4, 11, 15, 19, 12],
    4: [3, 2, 6, 7, 10, 14, 18, 15],
    5: [0, 1, 2, 3, 8, 9, 10, 11],
    6: [4, 5, 6, 7, 16, 17, 18, 19],
}

CONST["abgCoords"] = {
    0: [-1, 1, -1],
    1: [1, 1, -1],
    2: [1, -1, -1],
    3: [-1, -1, -1],

    4: [-1, 1, 1],
    5: [1, 1, 1],
    6: [1, -1, 1],
    7: [-1, -1, 1],

    8: [0, 1, -1],
    9: [1, 0, -1],
    10: [0, -1, -1],
    11: [-1, 0, -1],

    12: [-1, 1, 0],
    13: [1, 1, 0],
    14: [1, -1, 0],
    15: [-1, -1, 0],

    16: [0, 1, 1],
    17: [1, 0, 1],
    18: [0, -1, 1],
    19: [-1, 0, 1],
}

# 1D
CONST["gaussianCoords"] = [-sqrt(0.6), 0, sqrt(0.6)]
CONST["gaussianConsts"] = [5.0 / 9, 8.0 / 9, 5.0 / 9]

# 2D
CONST["gaussianNodes_2D"] = 9
CONST["gaussianCoords_2D"] = [[CONST["gaussianCoords"][x], CONST["gaussianCoords"][y]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])]

# 3D
CONST["gaussianNodes_3D"] = 27
CONST["gaussianCoords_3D"] = [[CONST["gaussianCoords"][x], CONST["gaussianCoords"][y], CONST["gaussianCoords"][z]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])
                              for z in range(CONST["axes"])]
CONST["gaussianConsts_3D"] = [[CONST["gaussianConsts"][x], CONST["gaussianConsts"][y], CONST["gaussianConsts"][z]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])
                              for z in range(CONST["axes"])]

CONST["e"] = 100
CONST["nu"] = 0.3
CONST["P"] = 20
CONST["mu"] = CONST["e"] / (2 * (1 + CONST["nu"]))
CONST["lambda"] = CONST["e"] / ((1 + CONST["nu"]) * (1 - 2 * CONST["nu"]))

CONST["mgeSize"] = 60

CONST["eta_tauAxes"] = 2
CONST["eta_tauNodes"] = 8
CONST["eta_tauCoords"] = {
    0: [-1, -1],
    1: [1, -1],
    2: [1, 1],
    3: [-1, 1],

    4: [0, -1],
    5: [1, 0],
    6: [0, 1],
    7: [-1, 0]
}

MATRICES = {}
MATRICES["AKT"] = []
MATRICES["NT"] = []
MATRICES["DFIABG"] = []
MATRICES["Jacobians"] = []
MATRICES["DFIXYZ"] = []
MATRICES["Jacobians_DET"] = []
MATRICES["a11"] = []
MATRICES["a12"] = []
MATRICES["a13"] = []
MATRICES["a22"] = []
MATRICES["a23"] = []
MATRICES["a33"] = []
MATRICES["MGE"] = []
MATRICES["DPSITE"] = []
MATRICES["MG"] = []
