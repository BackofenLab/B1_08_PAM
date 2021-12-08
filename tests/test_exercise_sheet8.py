from exercise_sheet8 import *


"""
a' = AAGTACTTT+AGGTAACACGTTTAGTCA+AAATTCCTA+AGTTTACCGGGTTAATCA
b' = AAATTCCTA+AGTTTACCGGGTTAATCA+AAGTACTTT+AGGTAACACGTTTAGTCA

Symmetric alignments are required to get symmetric counts in order to get a reversible Marov Chain model.
"""

def test_exercise_1a():
    r_A, r_C, r_T, r_G = exercise_1a()

    assert r_A == 0.333
    assert r_C == 0.167
    assert r_T == 0.333
    assert r_G == 0.167

def test_exercise_1b():
    """
    E_simplified =
    1/54 * [
        [ 12,    1,    3,  2],
        ["-",    6,    1,  1],
        ["-",  "-",   12,  2],
        ["-",  "-",  "-",  4]
    ]
    """
    E = exercise_1b()

    E_expected = [
        [0.222, 0.019, 0.056, 0.037],
        ["-",   0.111, 0.019, 0.019],
        ["-",     "-", 0.222, 0.037],
        ["-",     "-",   "-", 0.074]
    ]

    E_alt = [
        [0.222, 0.019, 0.056, 0.037],
        [0.019, 0.111, 0.019, 0.019],
        [0.056, 0.019, 0.222, 0.037],
        [0.037, 0.019, 0.037, 0.074]
    ]
    assert (E == E_expected) or (E == E_alt)

def test_exercise_1c():
    """
    Mismatch scoring is often negative, as mismatches are penalized
    """
    S = exercise_1c()

    S_expected = [
        [  3,   -5,   -3,  -2],
        ["-",    6,   -5,  -2],
        ["-",  "-",    3,  -2],
        ["-",  "-",  "-",   4]
    ]

    S_alt = [
        [ 3,  -5,  -3,  -2],
        [-5,   6,  -5,  -2],
        [-3,  -5,   3,  -2],
        [-2,  -2,  -2,   4]
    ]
    assert (S == S_expected) or (S == S_alt)

def test_exercise_1d():
    result = exercise_1d()


def test_exercise_1e():
    gamma = exercise_1e()

    assert gamma == 0.027

def test_exercise_1f():
    P = exercise_1f()

    P_expected = [
        [  0.667,  0.057,  0.168,  0.111],
        [  0.114,  0.665,  0.114,  0.114],
        [  0.168,  0.057,  0.667,  0.111],
        [  0.222,  0.114,  0.222,  0.443]
    ]

    assert P == P_expected

def test_exercise_1g():
    N = exercise_1g()

    N_expected = [
        [  0.9910,  0.0015,  0.0045,  0.0030],
        [  0.0031,  0.9907,  0.0031,  0.0031],
        [  0.0045,  0.0015,  0.9910,  0.0030],
        [  0.0060,  0.0031,  0.0060,  0.9849]
    ]

    assert N == N_expected

########################################################
############## Programming tasks #######################
########################################################
