from global_constants import *
from math import pow


def dfi_alpha_8(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.125 * (alpha_i * (1 + beta * beta_i) * (1 + gamma * gamma_i) * (alpha * alpha_i + beta * beta_i + gamma * gamma_i - 2) +
                    (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i) * alpha_i)


def dfi_beta_8(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.125 * ((1 + alpha * alpha_i) * beta_i * (1 + gamma * gamma_i) * (alpha * alpha_i + beta * beta_i + gamma * gamma_i - 2) +
                    (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i) * beta_i)


def dfi_gamma_8(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.125 * ((1 + alpha * alpha_i) * (1 + beta * beta_i) * gamma_i * (alpha * alpha_i + beta * beta_i + gamma * gamma_i - 2) +
                    (1 + alpha * alpha_i) * (1 + beta * beta_i) * (1 + gamma * gamma_i) * gamma_i)


def dfi_alpha_20(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.25 * (1 + beta * beta_i) * \
           (1 + gamma * gamma_i) * \
           (alpha_i -
            2 * alpha * pow(beta_i, 2) * pow(gamma_i, 2) -
            3 * pow(alpha, 2) * alpha_i * pow(beta_i, 2) * pow(gamma_i, 2) -
            alpha_i * pow(beta * alpha_i * gamma_i, 2) -
            alpha_i * pow(gamma * alpha_i * beta_i, 2))


def dfi_beta_20(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.25 * (1 + alpha * alpha_i) * \
           (1 + gamma * gamma_i) * \
           (beta_i -
            beta_i * pow(alpha * beta_i * gamma_i, 2) -
            2 * beta * pow(alpha_i, 2) * pow(gamma_i, 2) -
            3 * pow(beta, 2) * pow(alpha_i, 2) * beta_i * pow(gamma_i, 2) -
            beta_i * pow(gamma * alpha_i * beta_i, 2))


def dfi_gamma_20(alpha, beta, gamma, localIndex):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    return 0.25 * (1 + alpha * alpha_i) * \
           (1 + beta * beta_i) * \
           (gamma_i *
            (1 - pow(alpha * beta_i * gamma_i, 2) - pow(beta * alpha_i * gamma_i, 2)) -
            2 * gamma * pow(alpha_i, 2) * pow(beta_i, 2) -
            3 * pow(gamma, 2) * gamma_i * pow(alpha_i, 2) * pow(beta_i, 2))


def get_DFIABG():
    DFIABG_list = [
        [[0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["axes"])]
        for _ in range(CONST["gaussianNodes_3D"])]

    for gaussNode in range(CONST["gaussianNodes_3D"]):
        for localIndex in range(8):
            DFIABG_list[gaussNode][0][localIndex] = dfi_alpha_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)
            DFIABG_list[gaussNode][1][localIndex] = dfi_beta_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)
            DFIABG_list[gaussNode][2][localIndex] = dfi_gamma_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)
        for localIndex in range(8, 20):
            DFIABG_list[gaussNode][0][localIndex] = dfi_alpha_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)
            DFIABG_list[gaussNode][1][localIndex] = dfi_beta_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)
            DFIABG_list[gaussNode][2][localIndex] = dfi_gamma_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex)

    return DFIABG_list
