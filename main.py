from mg import get_MG
from plot import *
from akt_nt import *
from zu import *
from dfiabg import *
from dj import *
from dfixyz import *
from scipy.linalg import det
from mge import *
from dpsi import *

if __name__ == '__main__':
    MATRICES["AKT"] = get_AKT(CONST["size"], CONST["division"])
    MATRICES["NT"] = get_NT(CONST["division"], CONST["elementsNumber"])
    display_3d_grid([node.coords for node in MATRICES["AKT"]], MATRICES["NT"], get_ZU(MATRICES["AKT"], MATRICES["NT"]))

    # MATRICES["DFIABG"] = get_DFIABG()
    # MATRICES["Jacobians"] = [
    #     get_DJ(MATRICES["NT"], MATRICES["AKT"], MATRICES["DFIABG"], e)
    #     for e in range(CONST["elementsNumber"])]
    #
    # MATRICES["DFIXYZ"] = [
    #     get_DFIXYZ(MATRICES["Jacobians"][e], MATRICES["DFIABG"])
    #     for e in range(CONST["elementsNumber"])]
    #
    # MATRICES["Jacobians_DET"] = [
    #     [det(MATRICES["Jacobians"][e][gaussNode])
    #      for gaussNode in range(CONST["gaussianNodes_3D"])]
    #     for e in range(CONST["elementsNumber"])]
    #
    # for e in range(CONST["elementsNumber"]):
    #     MATRICES["a11"].append(get_a11(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #     MATRICES["a12"].append(get_a12(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #     MATRICES["a13"].append(get_a13(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #     MATRICES["a22"].append(get_a22(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #     MATRICES["a23"].append(get_a23(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #     MATRICES["a33"].append(get_a33(MATRICES["DFIXYZ"][e], MATRICES["Jacobians_DET"][e]))
    #
    # MATRICES["MGE"] = [get_MGE(MATRICES["a11"][e], MATRICES["a12"][e], MATRICES["a13"][e],
    #                            MATRICES["a22"][e], MATRICES["a23"][e],
    #                            MATRICES["a33"][e])
    #                    for e in range(CONST["elementsNumber"])]
    #
    # MATRICES["DPSITE"] = get_DPSITE()
    # MATRICES["MG"] = get_MG(MATRICES["MGE"], MATRICES["NT"], CONST["ZU"], MATRICES["AKT"])

    # print(MATRICES["MGE"])
