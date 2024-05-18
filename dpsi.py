from math import pow

from global_constants import CONST


def dpsi_eta_4(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return 0.25 * (1 + tau * tau_i) * (tau * tau_i * eta_i + 2 * eta * pow(eta_i, 2))


def dpsi_tau_4(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return 0.25 * (1 + eta * eta_i) * (eta * eta_i * tau_i + 2 * tau * pow(tau_i, 2))


def dpsi_eta_57(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return -eta * (1 + tau * tau_i)


def dpsi_tau_57(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return 0.5 * tau_i * (1 - pow(eta, 2))


def dpsi_eta_68(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return 0.5 * eta_i * (1 - pow(tau, 2))


def dpsi_tau_68(eta, tau, eta_tauIndex):
    eta_i, tau_i = CONST["eta_tauCoords"][eta_tauIndex]
    return -tau * (1 + eta * eta_i)


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
        [[0 for _ in range(CONST["eta_tauNodes"])]
         for _ in range(CONST["eta_tauAxes"])]
        for _ in range(CONST["gaussianNodes_2D"])]

    for gaussNode in range(CONST["gaussianNodes_2D"]):
        for eta_tauIndex in range(4):
            DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_eta_4(
                CONST["gaussianCoords_2D"][gaussNode][0],
                CONST["gaussianCoords_2D"][gaussNode][1],
                eta_tauIndex)
            DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_tau_4(
                CONST["gaussianCoords_2D"][gaussNode][0],
                CONST["gaussianCoords_2D"][gaussNode][1],
                eta_tauIndex)
        for eta_tauIndex in range(4, 8):
            if eta_tauIndex == 4 or eta_tauIndex == 6:
                DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_eta_57(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex)
                DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_tau_57(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex)

            if eta_tauIndex == 5 or eta_tauIndex == 7:
                DPSITE_list[gaussNode][0][eta_tauIndex] = dpsi_eta_68(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex)
                DPSITE_list[gaussNode][1][eta_tauIndex] = dpsi_tau_68(
                    CONST["gaussianCoords_2D"][gaussNode][0],
                    CONST["gaussianCoords_2D"][gaussNode][1],
                    eta_tauIndex)

        # DPSITE_list[gaussNode][0][4] = dpsi_eta_57(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     4)
        # DPSITE_list[gaussNode][1][4] = dpsi_tau_57(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     6)
        #
        # DPSITE_list[gaussNode][0][6] = dpsi_eta_57(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     6)
        # DPSITE_list[gaussNode][1][4] = dpsi_tau_57(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     6)
        #
        # DPSITE_list[gaussNode][0][5] = dpsi_eta_68(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     5)
        # DPSITE_list[gaussNode][1][5] = dpsi_tau_68(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     5)
        #
        # DPSITE_list[gaussNode][0][7] = dpsi_eta_68(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     7)
        # DPSITE_list[gaussNode][1][7] = dpsi_tau_68(
        #     CONST["gaussianCoords_2D"][gaussNode][0],
        #     CONST["gaussianCoords_2D"][gaussNode][1],
        #     7)

    return DPSITE_list
