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
    freq_matrix = [[x / sum_freq] for row in freq_matrix for x in row]
    return freq_matrix


def main():
    seq1 = "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA"
    seq2 = "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA"

    sim_align = seq1, seq2

    print(nucleotide_freq_calculation_correct(sim_align))
    print(mutation_calculation_correct(sim_align))


if __name__ == "__main__":
    main()
