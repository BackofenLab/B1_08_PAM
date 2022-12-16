from typing import runtime_checkable, Tuple, List
import numpy as np


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
