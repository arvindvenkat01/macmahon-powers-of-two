# MacMahon Powers of Two

This repository contains the Python code and data for the paper:

**"An Expository Note on MacMahon's Partition Statistics and the Elementary Detection of Powers of Two"**

* **Authors:** Arvind N. Venkat
  
This work has been archived and assigned a permanent identifier on Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17841690.svg)](https://doi.org/10.5281/zenodo.17841690)

### Pre-print:
* **DOI** - 10.5281/zenodo.17841690
* **URL** - https://zenodo.org/records/17841690

## Overview

This repository accompanies the expository note:

> *An Expository Note on MacMahon's Partition Statistics and the Elementary Detection of Powers of Two* (Venkat, 2025).

The note is inspired by Craig–van Ittersum–Ono’s work on how integer partitions detect the primes, and applies a simplified version of the same MacMahon framework to the much easier set of powers of two. The key point is to show, in a completely elementary way, how MacMahon’s first moment $M_1(n)$ (and a parity-restricted variant) can encode multiplicative structure when expressed via divisor sums.


## Contents

  - `verify_theorems.py` – Supplementary Python code to verify:
    - Theorem 1 (Power-of-two characterization using $M_1(n)$ and $M_1^{\text{odd}}(n)$.
    - Theorem 3 (Mersenne prime criterion combining the Craig–Ono prime detector with the power-of-two detector).


## Mathematical summary

- MacMahon’s first moment for one distinct part can be written as:
  
  $$M_1(n) = \sum_{d \mid n} \frac{n}{d} = \sigma_1(n)$$

  where $\sigma_1(n)$ is the usual sum-of-divisors function.

- Restricting to odd part sizes leads to:

  $$M_1^{\text{odd}}(n) = \sum_{\substack{d \mid n \\ d \text{ odd}}} \frac{n}{d}$$

  which, after writing $n = 2^k m$ with $m$ odd, simplifies to:

  $$M_1^{\text{odd}}(n) = 2^k \sigma_1(m)$$

- The expository note proves that the identity:

  $$(2n - 1) M_1^{\text{odd}}(n) - n M_1(n) = 0$$

  holds if and only if $n$ is a power of two.

- Combining this with the Craig–van Ittersum–Ono Level‑1 prime detector:

  $$L_{\text{prime}}(n) = (n^2 - 3n + 2)M_1(n) - 8M_2(n)$$

  yields a purely partition-theoretic criterion for Mersenne primes $n = 2^p - 1$.

The point of the project is expository rather than to claim a deep new theorem: powers of two are "visible" already at the level of $\sigma_1$, in contrast with primes, which require higher moments and quasimodular structure.


## Running the code

Requirements:

- Python 3.8+
- No external dependencies beyond the standard library.

To verify the theorems:

```bash
python verify_theorems.py
```


This will:

1. Precompute $\sigma_1(n)$, $\sigma_3(n)$, and the derived MacMahon moments $M_1(n), M_2(n), M_1^{\text{odd}}(n)$ up to `LIMIT` (default: 600000).
2. Check that the power-of-two identity holds if and only if \(n\) is a power of 2 in that range.
3. Apply the fused Mersenne prime criterion and print all detected Mersenne primes up to the chosen bound.

You can increase `LIMIT` in `verify_theorems.py` if you want to push the numerical verification further, at the cost of longer runtime.

## Expected Output
The script will precompute the necessary arithmetic tables and then scan for Mersenne primes. You should see output similar to this:
```bash
Generating partition data up to n=600000...

Scanning integers 2..600000 for Mersenne Primes...
Criterion: n is Prime AND n+1 is Power of 2
Formula:   (L_prime(n))^2 + (L_pow2(n+1))^2 == 0

FOUND MERSENNE PRIME #1: n = 3
FOUND MERSENNE PRIME #2: n = 7
FOUND MERSENNE PRIME #3: n = 31
FOUND MERSENNE PRIME #4: n = 127
FOUND MERSENNE PRIME #5: n = 8191
FOUND MERSENNE PRIME #6: n = 131071
FOUND MERSENNE PRIME #7: n = 524287
```

## Citation

If you use this code or note in your own work, you might cite it as:

@misc{naladiga_venkat_2025_17841690,
  author       = {Naladiga Venkat, Arvind},
  title        = {An Expository Note on MacMahon's Partition
                   Statistics and the Elementary Detection of Powers
                   of Two
                  },
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17841690},
  url          = {https://doi.org/10.5281/zenodo.17841690},
}

and optionally also cite Craig–van Ittersum–Ono for the primality detector:

> W. Craig, J.-W. van Ittersum, K. Ono, *Integer partitions detect the primes*, Proc. Natl. Acad. Sci. 121 (2024).


## License

MIT for code and CC BY 4.0 for the paper.

