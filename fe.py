import numpy as np

from dpsi import *
from global_constants import MATRICES


def get_FE_list(zp):
    FE_List = []
    zp_index = 0
    for i in range(CONST["elementsNumber"]):
        zp_item = next((item for item in CONST["ZP"] if item["element"] == i), None)
        if zp_item:
            FE_List.append(calculate_FE([CONST["gaussianConsts"][0], CONST["gaussianConsts"][1], CONST["gaussianConsts"][2]], CONST["P"], zp[zp_index], zp_item["side"]))
            zp_index += 1
        else:
            FE_List.append(np.zeros(60).tolist())
    return FE_List


def calculate_FE(gaussConstant, P, ZP, ZP_Side):  # zp is coords of this zp side, zp_side is a number of the side 1-6
    DxyzDnt_ = DxyzDnt(ZP)
    PSIxyz = get_PSI_xyz()
    fe1 = []
    fe2 = []
    fe3 = []
    for i in range(8):
        fe1_value = 0
        fe2_value = 0
        fe3_value = 0
        psi_index_from_depsi = 0
        for c_m in gaussConstant:
            for c_n in gaussConstant:
                DxyzDnt_item = DxyzDnt_[psi_index_from_depsi]
                PSIxyz_item = PSIxyz[psi_index_from_depsi][i]
                fe1_value += c_m * c_n * P * (DxyzDnt_item[1][0] * DxyzDnt_item[2][1] - DxyzDnt_item[2][0] * DxyzDnt_item[1][1]) * PSIxyz_item
                fe2_value += c_m * c_n * P * (DxyzDnt_item[2][0] * DxyzDnt_item[0][1] - DxyzDnt_item[0][0] * DxyzDnt_item[2][1]) * PSIxyz_item
                fe3_value += c_m * c_n * P * (DxyzDnt_item[0][0] * DxyzDnt_item[1][1] - DxyzDnt_item[1][0] * DxyzDnt_item[0][1]) * PSIxyz_item
                psi_index_from_depsi += 1
        fe1.append(fe1_value)
        fe2.append(fe2_value)
        fe3.append(fe3_value)

    return get_FE_60(fe1, fe2, fe3, ZP_Side)


def get_FE_60(fe1, fe2, fe3, ZP_Side):
    FE = [0 for _ in range(60)]
    fe1_indexes = [i for i in CONST["sideNTindexes"][ZP_Side]]
    fe2_indexes = [i + 20 for i in CONST["sideNTindexes"][ZP_Side]]
    fe3_indexes = [i + 40 for i in CONST["sideNTindexes"][ZP_Side]]

    for i in range(8):
        FE[fe1_indexes[i]] = fe1[i]

    for i in range(8):
        FE[fe2_indexes[i]] = fe2[i]

    for i in range(8):
        FE[fe3_indexes[i]] = fe3[i]

    return FE


def DxyzDnt(zp):  # zp is side which contains 8 points
    dxyzDnt = []
    depsite = MATRICES["DPSITE"]
    index_for_depsite = 0
    for _ in CONST["gaussianCoords"]:  # 3
        for _ in CONST["gaussianCoords"]:  # 3
            summ_x_eta = []
            summ_y_eta = []
            summ_z_eta = []
            summ_x_tau = []
            summ_y_tau = []
            summ_z_tau = []
            for point in zp:
                index_of_nt = zp.index(point)
                summ_x_eta.append(point[0] * depsite[index_for_depsite][0][index_of_nt])
                summ_y_eta.append(point[1] * depsite[index_for_depsite][0][index_of_nt])
                summ_z_eta.append(point[2] * depsite[index_for_depsite][0][index_of_nt])

                summ_x_tau.append(point[0] * depsite[index_for_depsite][1][index_of_nt])
                summ_y_tau.append(point[1] * depsite[index_for_depsite][1][index_of_nt])
                summ_z_tau.append(point[2] * depsite[index_for_depsite][1][index_of_nt])
            dxyzDnt.append([
                [sum(summ_x_eta), sum(summ_x_tau)],
                [sum(summ_y_eta), sum(summ_y_tau)],
                [sum(summ_z_eta), sum(summ_z_tau)]
            ])
            index_for_depsite += 1
    return dxyzDnt


def get_PSI_xyz():
    PSI = []
    for eta in CONST["gaussianCoords"]:
        for tau in CONST["gaussianCoords"]:
            a = []
            for i in CONST["eta_tauCoords"]:
                if i < 4:
                    a.append(psi_base_4(eta, tau, i))
                elif i == 4 or i == 6:
                    a.append(psi_base_57(eta, tau, i))
                elif i == 5 or i == 7:
                    a.append(psi_base_68(eta, tau, i))
            PSI.append(a)
    return PSI
