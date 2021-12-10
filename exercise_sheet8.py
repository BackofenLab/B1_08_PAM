from typing import runtime_checkable


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

    PAM2
    """


    return None


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
