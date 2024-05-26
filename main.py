from mg import get_MG
from plotting import *
from akt_nt import *
from zu import *
from zp import *
from dfiabg import *
from dj import *
from dfixyz import *
from scipy.linalg import det
from mge import *
from fe import *
from f import *
from akt_new import *

if __name__ == '__main__':
    MATRICES["AKT"] = get_AKT(CONST["size"], CONST["division"])
    MATRICES["NT"] = get_NT(CONST["division"], CONST["elementsNumber"])

    zu = get_ZU(MATRICES["AKT"], MATRICES["NT"])
    zp = get_ZP(MATRICES["AKT"], MATRICES["NT"])

    MATRICES["DFIABG"] = get_DFIABG()
    MATRICES["Jacobians"] = [
        get_DJ(MATRICES["NT"], MATRICES["AKT"], MATRICES["DFIABG"], e)
        for e in range(CONST["elementsNumber"])]

    MATRICES["DFIXYZ"] = [
        get_DFIXYZ(MATRICES["Jacobians"][e], MATRICES["DFIABG"])
        for e in range(CONST["elementsNumber"])]

    MATRICES["Jacobians_DET"] = [
        [det(MATRICES["Jacobians"][e][gaussNode])
         for gaussNode in range(CONST["gaussianNodes_3D"])]
        for e in range(CONST["elementsNumber"])]

    for e in range(CONST["elementsNumber"]):
        MATRICES["a11"].append(get_a11(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
        MATRICES["a12"].append(get_a12(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
        MATRICES["a13"].append(get_a13(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
        MATRICES["a22"].append(get_a22(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
        MATRICES["a23"].append(get_a23(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
        MATRICES["a33"].append(get_a33(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))

    MATRICES["MGE"] = [get_MGE(MATRICES["a11"][e], MATRICES["a12"][e], MATRICES["a13"][e],
                               MATRICES["a22"][e], MATRICES["a23"][e],
                               MATRICES["a33"][e])
                       for e in range(CONST["elementsNumber"])]

    MATRICES["MG"] = get_MG(MATRICES["MGE"], MATRICES["NT"], remove_duplicates_ZU(zu), MATRICES["AKT"])
    MATRICES["DPSITE"] = get_DPSITE()

    fe_list = get_FE_list(zp)
    F = get_F(fe_list, len(MATRICES["AKT"]), MATRICES["NT"])
    U = np.linalg.solve(MATRICES["MG"], F).tolist()
    new_AKT = get_AKT_modified(MATRICES["AKT"], U)
    new_ZP = get_ZP(new_AKT, MATRICES["NT"])
    display_3d_grid([node.coords for node in new_AKT], MATRICES["NT"], zu, new_ZP)
