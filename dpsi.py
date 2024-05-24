from math import pow
from global_constants import CONST
import sympy as sp


def dpsi_4(eta, tau, localIndex, respectTo):
    eta_i, tau_i = CONST["eta_tauCoords"][localIndex]
    eta_sym, tau_sym = sp.symbols('eta tau')
    eta_i_sym, tau_i_sym = sp.symbols('eta_i tau_i')
    psi_4 = (1 / 4) * (tau_sym * tau_i_sym + 1) * (eta_sym * eta_i_sym + 1) * (eta_sym * eta_i_sym + tau_i_sym * tau_sym - 1)

    if respectTo == "eta":
        derivative = sp.diff(psi_4, eta_sym)
    elif respectTo == "tau":
        derivative = sp.diff(psi_4, tau_sym)
    else:
        raise ValueError("Invalid respectTo value. Choose from 'eta' or 'tau'.")

    return float(derivative.subs({
        eta_sym: eta,
        tau_sym: tau,
        eta_i_sym: eta_i,
        tau_i_sym: tau_i,
    }))


def dpsi_57(eta, tau, localIndex, respectTo):
    eta_i, tau_i = CONST["eta_tauCoords"][localIndex]
    eta_sym, tau_sym = sp.symbols('eta tau')
    eta_i_sym, tau_i_sym = sp.symbols('eta_i tau_i')
    psi_57 = (1 / 2) * (1 - eta_sym ** 2) * (1 + tau_sym * tau_i_sym)

    if respectTo == "eta":
        derivative = sp.diff(psi_57, eta_sym)
    elif respectTo == "tau":
        derivative = sp.diff(psi_57, tau_sym)
    else:
        raise ValueError("Invalid respectTo value. Choose from 'eta' or 'tau'.")

    return float(derivative.subs({
        eta_sym: eta,
        tau_sym: tau,
        eta_i_sym: eta_i,
        tau_i_sym: tau_i,
    }))


def dpsi_68(eta, tau, localIndex, respectTo):
    eta_i, tau_i = CONST["eta_tauCoords"][localIndex]
    eta_sym, tau_sym = sp.symbols('eta tau')
    eta_i_sym, tau_i_sym = sp.symbols('eta_i tau_i')
    psi_68 = (1 / 2) * (1 - tau_sym ** 2) * (1 + eta_sym * eta_i_sym)

    if respectTo == "eta":
        derivative = sp.diff(psi_68, eta_sym)
    elif respectTo == "tau":
        derivative = sp.diff(psi_68, tau_sym)
    else:
        raise ValueError("Invalid respectTo value. Choose from 'eta' or 'tau'.")

    return float(derivative.subs({
        eta_sym: eta,
        tau_sym: tau,
        eta_i_sym: eta_i,
        tau_i_sym: tau_i,
    }))


def psi_base_4(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    result = (1 / 4) * (tau * tau_i + 1) * (eta * eta_i + 1) * (eta * eta_i + tau_i * tau - 1)
    return result


def psi_base_57(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    result = (1 / 2) * (-eta * eta + 1) * (tau_i * tau + 1)
    return result


def psi_base_68(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    result = (1 / 2) * (-tau * tau + 1) * (eta_i * eta + 1)
    return result


def get_DPSITE():
    DPSITE_list = [
        [[0.0 for _ in range(CONST["eta_tauNodes"])]  # 8
         for _ in range(CONST["eta_tauAxes"])]  # 2
        for _ in range(CONST["gaussianNodes_2D"])]  # 9

    for gaussNode in range(CONST["gaussianNodes_2D"]):
        for eta_tauIndex in range(4):
            DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_4(
                CONST["gaussianCoords_2D"][gaussNode][0],
                CONST["gaussianCoords_2D"][gaussNode][1],
                eta_tauIndex, "eta")
            DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_4(
                CONST["gaussianCoords_2D"][gaussNode][0],
                CONST["gaussianCoords_2D"][gaussNode][1],
                eta_tauIndex, "tau")
        for eta_tauIndex in range(4, 8):
            if eta_tauIndex == 4 or eta_tauIndex == 6:
                DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_57(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex, "eta")
                DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_57(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex, "tau")

            if eta_tauIndex == 5 or eta_tauIndex == 7:
                DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_68(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex, "eta")
                DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_68(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex, "tau")

    return DPSITE_list
