from math import log10

def helper_index(char):
    return "ACTG".index(char)


def nucleotide_freq_calculation_correct(sim_align):
    first_seq = sim_align[0]
    freq_list = [0] * 4
    for char in first_seq:
        index = helper_index(char)
        freq_list[index] += 1

    freq_list = [x / sum(freq_list) for x in freq_list]

    return freq_list


def mutation_calculation_correct(sim_align):
    seq1, seq2 = sim_align
    freq_matrix = [[0] * 4 for _ in range(4)]

    for char1, char2 in zip(seq1, seq2):
        index1, index2 = helper_index(char1), helper_index(char2)
        freq_matrix[index1][index2] += 1

    sum_freq = sum([x for row in freq_matrix for x in row])
    freq_matrix = [[x / sum_freq for x in row] for row in freq_matrix]
    return freq_matrix


def scores_calculation_correct(sim_align):
    freq_nuc = nucleotide_freq_calculation_correct(sim_align)
    freq_matrix = mutation_calculation_correct(sim_align)

    scores_matrix = [[freq_matrix[row_index][column_index] / (freq_nuc[row_index] * freq_nuc[column_index])
                      for column_index, column in enumerate(row)]
                     for row_index, row in enumerate(freq_matrix)]

    scores_matrix = [[round(10 * log10(x)) for x in row] for row in scores_matrix]
    return scores_matrix


def calculate_gamma(freq_mutations_matrix):
    sum_non_diagonal = sum([column for row_index, row in enumerate(freq_mutations_matrix)
                            for column_index, column in enumerate(row)
                            if row_index != column_index])
    gamma = 0.01 / sum_non_diagonal

    return gamma


def calculate_probabilities_correct(sim_align):
    freq_nuc = nucleotide_freq_calculation_correct(sim_align)
    freq_matrix = mutation_calculation_correct(sim_align)

    probability_matrix = [[freq_matrix[row_index][column_index] / (freq_nuc[row_index])
                           for column_index, column in enumerate(row)]
                          for row_index, row in enumerate(freq_matrix)]

    return probability_matrix


def calculate_norm_probabilities_correct(sim_align):
    probability_matrix = calculate_probabilities_correct(sim_align)
    freq_mutations = mutation_calculation_correct(sim_align)
    gamma = calculate_gamma(freq_mutations)

    probability_matrix = [[probability_matrix[row_index][column_index] * gamma
                           for column_index, column in enumerate(row)]
                          for row_index, row in enumerate(probability_matrix)]

    sum_non_diagonal = [sum([column for column_index, column in enumerate(row)
                             if row_index != column_index])
                        for row_index, row in enumerate(probability_matrix)]

    for index, _ in enumerate(probability_matrix):
        probability_matrix[index][index] = 1 - sum_non_diagonal[index]

    return probability_matrix


def main():
    seq1 = "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA"
    seq2 = "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA"

    sim_align = seq1, seq2

    print(nucleotide_freq_calculation_correct(sim_align))
    print(mutation_calculation_correct(sim_align))
    print(scores_calculation_correct(sim_align))

    m_matrix = mutation_calculation_correct(sim_align)
    print(calculate_gamma(m_matrix))

    print(calculate_probabilities_correct(sim_align))
    print(calculate_norm_probabilities_correct(sim_align))


if __name__ == "__main__":
    main()
