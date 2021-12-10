from exercise_sheet8 import *


"""
a' = AAGTACTTT+AGGTAACACGTTTAGTCA+AAATTCCTA+AGTTTACCGGGTTAATCA
b' = AAATTCCTA+AGTTTACCGGGTTAATCA+AAGTACTTT+AGGTAACACGTTTAGTCA

Symmetric alignments are required to get symmetric counts in order to get a reversible Marov Chain model.
"""

def test_exercise_1a():
    r_A, r_C, r_T, r_G = exercise_1a()

    assert r_A == 0.3333
    assert r_C == 0.1667
    assert r_T == 0.3333
    assert r_G == 0.1667

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
        [0.2222, 0.0185, 0.0556, 0.0370],
        ["-",    0.1111, 0.0185, 0.0185],
        ["-",       "-", 0.2222, 0.0370],
        ["-",       "-",    "-", 0.0741]
    ]

    E_alt = [
        [0.2222, 0.0185, 0.0556, 0.0370],
        [0.0185, 0.1111, 0.0185, 0.0185],
        [0.0556, 0.0185, 0.2222, 0.0370],
        [0.0370, 0.0185, 0.0370, 0.0741]
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
        [  0.6667,  0.0555,  0.1668,  0.1110],
        [  0.1110,  0.6665,  0.1110,  0.1110],
        [  0.1668,  0.0555,  0.6667,  0.1110],
        [  0.2220,  0.1110,  0.2220,  0.4445]
    ]

    assert P == P_expected

def test_exercise_1g():
    N = exercise_1g()

    N_expected = [
        [  0.9910,  0.0015,  0.0045,  0.0030],
        [  0.0030,  0.9910,  0.0030,  0.0030],
        [  0.0045,  0.0015,  0.9910,  0.0030],
        [  0.0060,  0.0030,  0.0060,  0.9850]
    ]

    assert N == N_expected

def test_exercise_1h():
    PAM1 = exercise_1h()

    PAM1_expected = [
        [  5,  -20,  -19,  -17],
        ["-",    8,  -20 , -17],
        ["-",  "-",    5,  -17],
        ["-",  "-",  "-",    8]
    ]

    PAM1_alt = [
        [  5,  -20,  -19,  -17],
        [-20,    8,  -20 , -17],
        [-19,  -20,    5,  -17],
        [-17,  -17,  -17,    8]
    ]
    assert (PAM1 == PAM1_expected) or (PAM1 == PAM1_alt)

def test_exercise_1i():
    PAM2 = exercise_1i()

    PAM2_expected = [
        [  5,  -17,  -16,  -15],
        ["-",    8,  -17 , -15],
        ["-",  "-",    5,  -15],
        ["-",  "-",  "-",    8]
    ]

    PAM2_alt = [
        [  5,  -17,  -16,  -15],
        [-17,    8,  -17 , -15],
        [-16,  -17,    5,  -15],
        [-15,  -15,  -15,    8]
    ]

    assert (PAM2 == PAM2_expected) or (PAM2 == PAM2_alt)


########################################################
############## Programming tasks #######################
########################################################
