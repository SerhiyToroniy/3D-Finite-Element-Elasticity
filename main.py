from node_indices import *
from DFI import *
from plotting import display_3d_grid

if __name__ == '__main__':
    MATRICES["AKT"] = get_AKT(CONST["size"], CONST["division"])
    MATRICES["NT"] = get_NT(CONST["division"], CONST["elementsNumber"])
    MATRICES["DFIABG"] = get_DFIABG()

    display_3d_grid([node.coords for node in MATRICES["AKT"]])
