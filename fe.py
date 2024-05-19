import numpy as np

from global_constants import CONST, MATRICES
from dpsi import *


def get_FE(zp):
    FE = []
    zp_index = 0
    for i in range(CONST["elementsNumber"]):
        if any(item["element"] == i for item in CONST["ZP"]):
            FE.append(calculate_FE([CONST["gaussianConsts"][0], CONST["gaussianConsts"][1], CONST["gaussianConsts"][2]], CONST["P"], zp[zp_index]))
            zp_index += 1
        else:
            FE.append(np.zeros(60).tolist())
    return FE


def calculate_FE(gaussConstant, P, ZP):
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
        for m in gaussConstant:
            for n in gaussConstant:
                DxyzDnt_item = DxyzDnt_[psi_index_from_depsi]
                PSIxyz_item = PSIxyz[psi_index_from_depsi][i]
                fe1_value += m * n * P * (DxyzDnt_item[1][0] * DxyzDnt_item[2][1] - DxyzDnt_item[2][0] * DxyzDnt_item[1][1]) * PSIxyz_item
                fe2_value += m * n * P * (DxyzDnt_item[2][0] * DxyzDnt_item[0][1] - DxyzDnt_item[0][0] * DxyzDnt_item[2][1]) * PSIxyz_item
                fe3_value += m * n * P * (DxyzDnt_item[0][0] * DxyzDnt_item[1][1] - DxyzDnt_item[1][0] * DxyzDnt_item[0][1]) * PSIxyz_item
                psi_index_from_depsi += 1
        fe1.append(fe1_value)
        fe2.append(fe2_value)
        fe3.append(fe3_value)

    Fe = [
        0, 0, 0, 0,
        fe1[0], fe1[1], fe1[2], fe1[3],
        0, 0, 0, 0,
        0, 0, 0, 0,
        fe1[4], fe1[5], fe1[6], fe1[7],
        0, 0, 0, 0,
        fe2[0], fe2[1], fe2[2], fe2[3],
        0, 0, 0, 0,
        0, 0, 0, 0,
        fe2[4], fe2[5], fe2[6], fe2[7],
        0, 0, 0, 0,
        fe3[0], fe3[1], fe3[2], fe3[3],
        0, 0, 0, 0,
        0, 0, 0, 0,
        fe3[4], fe3[5], fe3[6], fe3[7]
    ]

    return Fe


def DxyzDnt(zp):
    result = []
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
            result.append([
                [sum(summ_x_eta), sum(summ_x_tau)],
                [sum(summ_y_eta), sum(summ_y_tau)],
                [sum(summ_z_eta), sum(summ_z_tau)]
            ])
            index_for_depsite += 1
    return result


def get_PSI_xyz():
    result = []
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
            result.append(a)
    return result
