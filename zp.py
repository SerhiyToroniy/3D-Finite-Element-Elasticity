from global_constants import CONST


def get_ZP(AKT, NT):
    zp = []

    for side in CONST["ZP"]:
        local_coords = NT[side["element"]]
        surface_indexes = CONST["sideNTindexes"][side["side"]]
        zp.append([AKT[local_coords[i]].coords for i in surface_indexes])

    return zp
