from global_constants import CONST


def get_ZU(AKT, NT):
    zu = []
    for side in CONST["ZU"]:
        local_coords = NT[side["element"]]
        surface_indexes = CONST["sideNTindexes"][side["side"]]
        zu.append([AKT[local_coords[i]].coords for i in surface_indexes])

    return zu
