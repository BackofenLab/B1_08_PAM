from typing import runtime_checkable, Tuple, List
import numpy as np

def exercise_1a():
    """
    Exercise 1 a

    Calculate the nucleotide frequencies r_x.
    """

    r_A = 0.0000
    r_C = 0.0000
    r_T = 0.0000
    r_G = 0.0000

    return r_A, r_C, r_T, r_G


def exercise_1b():
    """
    Exercise 1 b

    Calculate the symmetric mutation probability matrix E(x,y).
    """

    E = [#A       #C       #T       #G
        [0.0000,  0.0000,  0.0000,  0.0000], #A
        [   "-",  0.0000,  0.0000,  0.0000], #C
        [   "-",     "-",  0.0000,  0.0000], #T
        [   "-",     "-",     "-",  0.0000]  #G
    ]

    return E

def exercise_1c():
    """
    Exercise 1 c

    Calculate the non-normalized PAM matrix S with 10*log<sub>10</sub>(odds),
    using the previously determined r values and E matrix. (round to integers)
    """

    S = [ #A    #C    #T   #G
        [  0,    0,    0,   0], #A
        ["-",    0,    0,   0], #C
        ["-",  "-",    0,   0], #T
        ["-",  "-",  "-",   0]  #G
    ]

    return S

def exercise_1d():
    """
    Exercise 1 d

    Given the sequences a = ACC and b = ATT, compute the optimal Needleman-Wunsch alignments using:
    1. The general similarity function.
    2. The PAM1-based similarity scoring function.
    
    Set the correct answers to True and the wrong answers to False
    """

    A = None

    B = None

    C = None

    D = None

    return A, B, C, D


def exercise_1e():
    """
    Exercise 1 e

    Calculate the normalization factor γ based on E.
    """

    gamma = 0.000

    return gamma

def exercise_1f():
    """
    Exercise 1 f

    Calculate the mutation rate matrix P.
    """

    P = [  #A       #C       #T       #G
        [  0.0000,  0.0000,  0.0000,  0.0000], #A
        [  0.0000,  0.0000,  0.0000,  0.0000], #C
        [  0.0000,  0.0000,  0.0000,  0.0000], #T
        [  0.0000,  0.0000,  0.0000,  0.0000]  #G
    ]

    return P

def exercise_1g():
    """
    Exercise 1 g

    Calculate the normalized mutation rate matrix P' using P and factor γ.
    """

    P_prime = [  #A       #C       #T       #G
        [  0.0000,  0.0000,  0.0000,  0.0000], #A
        [  0.0000,  0.0000,  0.0000,  0.0000], #C
        [  0.0000,  0.0000,  0.0000,  0.0000], #T
        [  0.0000,  0.0000,  0.0000,  0.0000]  #G
    ]
    return P_prime


def exercise_1h():
    """
    Exercise 1 h

    Determine PAM1 based on the normalized mutation rate matrix N with 10*log_10(odds)
    (round to integer)
    """

    PAM1 = [ #A    #C    #T   #G
           [  0,    0,    0,   0], #A
           ["-",    0,    0,   0], #C
           ["-",  "-",    0,   0], #T
           ["-",  "-",  "-",   0]  #G
    ]
    return PAM1

def exercise_1i():
    """
    Exercise 1 i

    Determine PAM2.
    (round to integer)
    """

    PAM2 = [ #A    #C    #T   #G
           [  0,    0,    0,   0], #A
           ["-",    0,    0,   0], #C
           ["-",  "-",    0,   0], #T
           ["-",  "-",  "-",   0]  #G
    ]

    return PAM2

########################################################
############## Programming tasks #######################
########################################################


def nucleotide_freq_calculation(sym_align: Tuple[str, str]) -> List[float]:
    """
    Implement the calculation of the nucleotide frequencies for a symmetric
    alignment. Make sure that the indexing works the followin way:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    sym align: Tuple of strings representing the symmetric alignment
    """
    first_seq, second_seq = sym_align
    freq_list = []  # Frequencies should be in order A,C,T,G
    return freq_list


def mutation_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of the mutations remember indexing in any
    dimension should be done in order:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    Hint: You can use your already implemented functions here
    """
    first_seq, second_seq = sym_align
    freq_matrix = [[0] * 4 for _ in range(4)]
    return freq_matrix


def scores_calculation(sym_align: Tuple[str, str]) -> List[List[int]]:
    """
    Implement the calculation of the scores remember indexing in any
    dimension should be done in order:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    Hint: You can use your already implemented functions here
    """
    score_matrix = None
    return score_matrix


def gamma_calculation(sym_align: Tuple[str, str]) -> float:
    """
    Implement the calculation of gamma.
    Hint: You can use your already implemented functions here
    """
    gamma = None
    return gamma


def probabilities_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of probabilities matrix.
    Hint: You can use your already implemented functions here
    """
    probability_matrix = None
    return probability_matrix


def norm_probabilities_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of normalized probabilities matrix.
    Hint: You can use your already implemented functions here
    """
    norm_matrix = None
    return norm_matrix


def pam_calculation(sym_align: Tuple[str, str], power: int) -> List[List[int]]:
    """
    Implement the calculation of pam matrix Make sure to round values to
    integers. ( Notice that casting to int does not do the correct
    rounding)
    power: the power of the PAM matrix e.g. PAM1 or PAM250
    Hint: You can use your already implemented functions here
    """
    pam = None
    return pam
