from global_constants import *
import sympy as sp


def dfi_8(alpha, beta, gamma, localIndex, respectTo):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    alpha_sym, beta_sym, gamma_sym = sp.symbols('alpha beta gamma')
    alpha_i_sym, beta_i_sym, gamma_i_sym = sp.symbols('alpha_i beta_i gamma_i')
    fi_8 = 0.125 * ((1 + alpha_sym * alpha_i_sym) * (1 + beta_sym * beta_i_sym) *
                    (1 + gamma_sym * gamma_i_sym) * (alpha_sym * alpha_i_sym + beta_sym * beta_i_sym + gamma_sym * gamma_i_sym - 2))

    if respectTo == "alpha":
        derivative = sp.diff(fi_8, alpha_sym)
    elif respectTo == "beta":
        derivative = sp.diff(fi_8, beta_sym)
    elif respectTo == "gamma":
        derivative = sp.diff(fi_8, gamma_sym)
    else:
        raise ValueError("Invalid respectTo value. Choose from 'alpha', 'beta', or 'gamma'.")

    return float(derivative.subs({
        alpha_sym: alpha,
        beta_sym: beta,
        gamma_sym: gamma,
        alpha_i_sym: alpha_i,
        beta_i_sym: beta_i,
        gamma_i_sym: gamma_i,
    }))


def dfi_20(alpha, beta, gamma, localIndex, respectTo):
    alpha_i, beta_i, gamma_i = CONST["abgCoords"][localIndex]
    alpha_sym, beta_sym, gamma_sym = sp.symbols('alpha beta gamma')
    alpha_i_sym, beta_i_sym, gamma_i_sym = sp.symbols('alpha_i beta_i gamma_i')
    fi_20 = 0.25 * ((1 + alpha_sym * alpha_i_sym) * (1 + beta_sym * beta_i_sym) * (1 + gamma_sym * gamma_i_sym) *
                    (1 - (alpha_sym * beta_i_sym * gamma_i_sym) ** 2 - (beta_sym * alpha_i_sym * gamma_i_sym) ** 2 - (gamma_sym * alpha_i_sym * beta_i_sym) ** 2))

    if respectTo == "alpha":
        derivative = sp.diff(fi_20, alpha_sym)
    elif respectTo == "beta":
        derivative = sp.diff(fi_20, beta_sym)
    elif respectTo == "gamma":
        derivative = sp.diff(fi_20, gamma_sym)
    else:
        raise ValueError("Invalid respectTo value. Choose from 'alpha', 'beta', or 'gamma'.")

    new = float(derivative.subs({
        alpha_sym: alpha,
        beta_sym: beta,
        gamma_sym: gamma,
        alpha_i_sym: alpha_i,
        beta_i_sym: beta_i,
        gamma_i_sym: gamma_i,
    }))
    return new


def get_DFIABG():
    DFIABG_list = [
        [[0.0 for _ in range(CONST["localNodes"])]
         for _ in range(CONST["axes"])]
        for _ in range(CONST["gaussianNodes_3D"])]

    for gaussNode in range(CONST["gaussianNodes_3D"]):
        for localIndex in range(8):
            DFIABG_list[gaussNode][0][localIndex] = dfi_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "alpha")
            DFIABG_list[gaussNode][1][localIndex] = dfi_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "beta")
            DFIABG_list[gaussNode][2][localIndex] = dfi_8(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "gamma")
        for localIndex in range(8, 20):
            DFIABG_list[gaussNode][0][localIndex] = dfi_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "alpha")
            DFIABG_list[gaussNode][1][localIndex] = dfi_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "beta")
            DFIABG_list[gaussNode][2][localIndex] = dfi_20(
                CONST["gaussianCoords_3D"][gaussNode][0],
                CONST["gaussianCoords_3D"][gaussNode][1],
                CONST["gaussianCoords_3D"][gaussNode][2],
                localIndex, "gamma")

    return DFIABG_list
