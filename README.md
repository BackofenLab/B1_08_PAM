Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 8: Substitution Scoring
---
### _Exercise 1 - Point Accepted Mutation (PAM)_
We want to calculate the PAM1 matrix based on the following two sequence alignments of the DNA sequences a, b, c and d.

<p align="center">
  <img src="./figures/sheet8-exercise1-sequences.svg" alt="sequences" width=70%/>
</p>


Tip: In order to solve **a)** and **b)** create a combined alignment comprised of two combined sequences a' and b' (based on the two initial alignments and their symetric counterparts)
<details>
  <summary>Hint: (Click to open)</summary>
  a' = a + c + b + d

  b' = b + d + a + c

  The order does not matter, as the frequency identification is position-insensitive.
</details>

Unless otherwise stated round all results to 4 decimal places.

**a)** Calculate the nucleotide frequencies r<sub>x</sub>.
<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-r.svg" alt="r" width=20%/>
  </p>

</details>

**b)** Calculate the symmetric mutation probability matrix E(x,y).

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-E.svg" alt="E" width=40%/>
  </p>

</details>

**c)** Calculate the non-normalized PAM matrix S with 10*log<sub>10</sub>(odds), using the previously determined r values and E matrix. (round to integers)

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-S.svg" alt="S" width=35%/>
  </p>

</details>

**d)** Given the sequences _a_ = ACC and _b_ = ATT, compute the optimal Needleman-Wunsch alignments using:

1. The general similarity scoring function.

<p align="center">
    <img src="./figures/sheet8-exercise1-D-general.svg" alt="General" width=90%/>
  </p>
    
2. The PAM1-based similarity scoring function.

<p align="center">
    <img src="./figures/sheet8-exercise1-D-PAM1.svg" alt="PAM1" width=90%/>
</p>

where _s_<sub>x,y</sub> are entries from the non-normalized PAM matrix S from above.

Select the correct answer based on the obtained results.

<p align="center">
    <img src="./figures/sheet8-exercise1-D-result.svg" alt="Results" width=100%/>
</p>
    
**e)** Calculate the normalization factor γ based on E.

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-gamma.svg" alt="Gamma" width=50%/>
  </p>

</details>

**f)** Calculate the mutation rate matrix P.

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-P.svg" alt="P" width=15%/>
  </p>

</details>

**g)** Calculate the normalized mutation rate matrix P' using P and the normalization factor γ.

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-pprime.svg" alt="pprime" width=25%/>
  </p>

</details>

**h)** Determine PAM1 based on the normalized mutation rate matrix P' with 10*log<sub>10</sub>(odds) (round to integer)

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-PAM1.svg" alt="PAM1" width=35%/>
  </p>

</details>

**i)** Determine PAM2. (round to integer)

<details>
  <summary>Formula: (Click to open)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-PAMX.svg" alt="PAMX" width=40%/>
  </p>

</details>

### _Exercise 2 - Programming assignmnet: Substitution Scoring Models_

**a)** Implement the calculation of the nucleotide frequencies for a symmetric alignment. Make sure that the indexing works the followin way:

- [0] = A
- [1] = C
- [2] = T
- [3] = G

**b)** Implement the calculation of the mutations. Remember indexing as in the previous exercise.

**c)** Implement the calculation of the scores. Remember indexing as in the previous exercise.

**d)** Implement the calculation of gamma.

**e)** Implement the calculation of probabilities matrix.

**f)** Implement the calculation of normalized probabilities matrix.

**g)** Implement the calculation of the PAM matrix. Make sure to round values to integers.