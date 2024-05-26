from global_constants import *
from node import Node


def get_AKT(size, division):
    layersNumber = 2 * division["z"] + 1
    xyzSteps = [s / (2 * d) for s, d in
                zip(size.values(), division.values())]
    AKT_list = []

    for layer in range(layersNumber):
        if layer % 2 == 0:
            for row in range(2 * division["y"] + 1):
                if row % 2 == 0:
                    for nodes in range(2 * division["x"] + 1):
                        AKT_list.append(Node(coords=[nodes * xyzSteps[0],
                                                     row * xyzSteps[1],
                                                     layer * xyzSteps[2]]))
                else:
                    for nodes in range(division["x"] + 1):
                        AKT_list.append(Node(coords=[nodes * xyzSteps[0] * 2,  # from left to right double size step
                                                     row * xyzSteps[1],
                                                     layer * xyzSteps[2]]))
        else:
            for row in range(division["y"] + 1):
                for nodes in range(division["x"] + 1):
                    AKT_list.append(Node(coords=[nodes * xyzSteps[0] * 2,  # from left to right double size step
                                                 row * xyzSteps[1] * 2,  # from front to back double size step
                                                 layer * xyzSteps[2]]))

    return AKT_list


def get_NT(division, elementsNumber):
    fullRowNodes = 2 * division["x"] + 1
    midRowNodes = division["x"] + 1

    fullLayerNodes = ((fullRowNodes + midRowNodes) *
                      division["y"]) + fullRowNodes
    midLayerNodes = midRowNodes * (division["y"] + 1)

    bothRowsNodes = fullRowNodes + midRowNodes
    bothLayersNodes = fullLayerNodes + midLayerNodes

    cubesPerLayer = division["x"] * division["y"]
    NT_list = [
        [0 for _ in range(CONST["localNodes"])]
        for _ in range(elementsNumber)]

    for z in range(division["z"]):
        for y in range(division["y"]):
            for x in range(division["x"]):
                scaleZ = z * bothLayersNodes
                scaleY = y * bothRowsNodes

                cubeIndex = cubesPerLayer * z + division["x"] * y + x

                # bottom layer corners
                NT_list[cubeIndex][0] = scaleZ + scaleY + x * 2
                NT_list[cubeIndex][1] = NT_list[cubeIndex][0] + 2
                NT_list[cubeIndex][2] = NT_list[cubeIndex][1] + bothRowsNodes
                NT_list[cubeIndex][3] = NT_list[cubeIndex][2] - 2

                # upper layer corners
                for i in range(4, 8):
                    NT_list[cubeIndex][i] = NT_list[cubeIndex][i - 4] + bothLayersNodes

                # bottom layer mids
                NT_list[cubeIndex][8] = NT_list[cubeIndex][0] + 1
                NT_list[cubeIndex][9] = scaleZ + scaleY + fullRowNodes + x + 1  # +1 beacuse index starts from 0
                NT_list[cubeIndex][10] = NT_list[cubeIndex][8] + bothRowsNodes
                NT_list[cubeIndex][11] = NT_list[cubeIndex][9] - 1

                # mid mids
                NT_list[cubeIndex][12] = scaleZ + fullLayerNodes + y * midRowNodes + x
                NT_list[cubeIndex][13] = NT_list[cubeIndex][12] + 1
                NT_list[cubeIndex][14] = NT_list[cubeIndex][13] + midRowNodes
                NT_list[cubeIndex][15] = NT_list[cubeIndex][14] - 1

                # upper layer mids
                for i in range(16, 20):
                    NT_list[cubeIndex][i] = NT_list[cubeIndex][i - 8] + bothLayersNodes

    return NT_list
