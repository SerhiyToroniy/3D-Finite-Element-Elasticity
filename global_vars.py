from math import sqrt

CONST = {}

CONST["axes"] = 3
CONST["size"] = {"x": 2, "y": 1, "z": 2}
CONST["division"] = {"x": 2, "y": 1, "z": 2}

CONST["elementsNumber"] = CONST["division"]["x"] * \
    CONST["division"]["y"] * \
    CONST["division"]["z"]

CONST["localNodes"] = 20

CONST["ZU"] = [{"element": 0, "side": 5},
               {"element": 1, "side": 5}]
CONST["ZP"] = [{"element": 2, "side": 6, "force": 2},
               {"element": 3, "side": 6, "force": 2}]

CONST["abgCoords"] = {
    0: [-1, -1, -1],
    1: [1, -1, -1],
    2: [1, 1, -1],
    3: [-1, 1, -1],

    4: [-1, -1, 1],
    5: [1, -1, 1],
    6: [1, 1, 1],
    7: [-1, 1, 1],

    8: [0, -1, -1],
    9: [1, 0, -1],
    10: [0, 1, -1],
    11: [-1, 0, -1],

    12: [-1, -1, 0],
    13: [1, -1, 0],
    14: [1, 1, 0],
    15: [-1, 1, 0],

    16: [0, -1, 1],
    17: [1, 0, 1],
    18: [0, 1, 1],
    19: [-1, 0, 1],
}

CONST["gaussianCoords"] = [-sqrt(0.6),
                           0,
                           sqrt(0.6)]
CONST["gaussianConsts"] = [5.0/9,
                           8.0/9,
                           5.0/9]
CONST["gaussianNodes_3D"] = 27
CONST["gaussianNodes_2D"] = 9

CONST["gaussianCoords_2D"] = [[CONST["gaussianCoords"][x], CONST["gaussianCoords"][y]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])]

CONST["gaussianCoords_3D"] = [[CONST["gaussianCoords"][x], CONST["gaussianCoords"][y], CONST["gaussianCoords"][z]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])
                              for z in range(CONST["axes"])]

CONST["gaussianConsts_3D"] = [[CONST["gaussianConsts"][x], CONST["gaussianConsts"][y], CONST["gaussianConsts"][z]]
                              for x in range(CONST["axes"])
                              for y in range(CONST["axes"])
                              for z in range(CONST["axes"])]


MATRICES = {}
MATRICES["AKT"] = []
MATRICES["NT"] = []
MATRICES["DFIABG"] = []
