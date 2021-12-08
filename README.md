Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 8: Point Accepted Mutation (PAM)
---
### _Exercise 1 - PAM_
We want to calculate the PAM1 matrix based on the following two sequence alignments of the DNA sequences a, b, c and d.

<p align="center">
  <img src="./figures/sheet8-exercise1-sequences.svg" alt="sequences" width=100%/>
</p>


Tip: In order to solve **a)** and **b)** create a combined alignment comprised of two combined sequences a' and b' (based on the two initial alignments and their symetric counterparts)
<details>
  <summary>Example: (Spoiler)</summary>
  a' = a + c + b + d
  b' = b + d + a + c

  The order does not matter, as the frequency identification is position-insensitive.
</details>

Unless otherwise stated round all results to 4 decimal places.

**a)** Calculate the nucleotide frequencies r<sub>x</sub>.
<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-r.svg" alt="r" width=100%/>
  </p>

</details>

**b)** Calculate the symmetric mutation probability matrix E(x,y).

<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-E.svg" alt="E" width=100%/>
  </p>

</details>

**c)** Calculate the non-normalized PAM matrix S with 10*log<sub>10</sub>(odds), using the previously determined r values and E matrix. (round to integers)

<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-S.svg" alt="S" width=100%/>
  </p>

</details>

**d)**

**e)** Calculate the normalization factor γ based on E.

<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-gamma.svg" alt="Gamma" width=100%/>
  </p>

</details>

**f)** Calculate the mutation rate matrix P.

<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-P.svg" alt="P" width=100%/>
  </p>

</details>

**g)** Calculate the normalized mutation rate matrix N using P and factor γ.

<details>
  <summary>Formula: (Spoiler)</summary>
  <p align="center">
    <img src="./figures/sheet8-exercise1-N.svg" alt="N" width=100%/>
  </p>

</details>
