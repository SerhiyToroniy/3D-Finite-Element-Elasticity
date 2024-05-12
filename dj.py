from global_constants import CONST


def get_DJ(NT, AKT, DFIABG, element):
    elementJacobian_list = [
        [[0 for _ in range(CONST["axes"])]
         for _ in range(CONST["axes"])]
        for _ in range(CONST["gaussianNodes_3D"])]

    for gaussNode in range(CONST["gaussianNodes_3D"]):
        for localAxis in range(CONST["axes"]):
            for globalAxis in range(CONST["axes"]):
                for localIndex in range(CONST["localNodes"]):
                    global_index = NT[element][localIndex]
                    elementJacobian_list[gaussNode][localAxis][globalAxis] += AKT[global_index].coords[globalAxis] * DFIABG[gaussNode][localAxis][localIndex]
    return elementJacobian_list
