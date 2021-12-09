def nucleotide_freq_calculation_correct(sim_align):
    first_seq = sim_align[0]
    freq_list = [0] * 4
    for char in first_seq:
        index = "ACTG".index(char)
        freq_list[index] += 1

    freq_list = [x / sum(freq_list) for x in freq_list]

    return freq_list


def main():
    seq1 = "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA"
    seq2 = "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA"

    sim_align = seq1, seq2

    print(nucleotide_freq_calculation_correct(sim_align))


if __name__ == "__main__":
    main()