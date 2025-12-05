import sys

# ==========================================
# 1. DATA GENERATION (ARITHMETIC THEOREMS)
# ==========================================
def compute_tables(limit_n):
    """
    Computes MacMahon functions using their Arithmetic Divisor Sum identities.
    
    DEFINITIONS:
    M1(n)     = Sum of Multiplicities of partitions with 1 distinct part size.
                = Sum(n/d) for all d|n
                = Sum(d)   for all d|n  (Identical to sigma_1(n))
                
    M1_odd(n) = Sum of Multiplicities of partitions where the distinct part is ODD.
                = Sum(n/d) for all d|n where d is ODD.
                != Sum(d)   for all d|n where d is ODD (This would be sigma_odd).
                
                Derivation:
                Let n = 2^k * m (where m is odd).
                The odd divisors d of n are exactly the divisors of m.
                The term is n/d = (2^k * m) / d = 2^k * (m/d).
                Summing this gives: 2^k * sigma_1(m).
    """
    print(f"Generating partition data up to n={limit_n}...")
    
    # 1. Sieve for standard Divisor Sums (sigma_1, sigma_3)
    sigma1 = [0] * (limit_n + 1)
    sigma3 = [0] * (limit_n + 1)
    
    for d in range(1, limit_n + 1):
        d3 = d**3
        for n in range(d, limit_n + 1, d):
            sigma1[n] += d
            sigma3[n] += d3
            
    # 2. Convert to MacMahon Values
    M1 = sigma1
    M2 = [0] * (limit_n + 1)
    M1_odd = [0] * (limit_n + 1)
    
    for n in range(1, limit_n + 1):
        # M2 Formula (Craig/Rose/Ono)
        # M2(n) = ((1 - 2n)*sigma1(n) + sigma3(n)) / 8
        M2[n] = ((1 - 2*n) * sigma1[n] + sigma3[n]) // 8
        
        # M1_odd Formula (Corrected Definition)
        # We need 2^k * sigma1(m)
        m = n
        shift = 1
        while m % 2 == 0:
            m //= 2
            shift *= 2
        
        # shift is 2^k. sigma1[m] is sum of divisors of the odd part.
        M1_odd[n] = shift * sigma1[m]
        
    return M1, M2, M1_odd

# ==========================================
# 2. THE DETECTOR POLYNOMIALS
# ==========================================

# COMPONENT A: PRIMALITY (Craig et al.)
# Relies on M1 and M2.
# Formula found via LLL: 8*M2 - (n^2 - 3n + 2)*M1 = 0  IFF n is Prime
def L_prime(n, M1, M2):
    # 8*M2 - (n-1)(n-2)M1
    term_m2 = 8 * M2[n]
    term_m1 = (n**2 - 3*n + 2) * M1[n]
    return term_m2 - term_m1

# COMPONENT B: POWER OF 2 (Your Discovery)
# Relies on M1 and M1_odd.
# Formula: (2m-1)*M1_odd(m) - m*M1(m) = 0  IFF m is Power of 2
def L_pow2(m, M1, M1_odd):
    return (2*m - 1)*M1_odd[m] - m*M1[m]

# ==========================================
# 3. THE MERSENNE SCAN
# ==========================================
def find_mersenne_primes(limit_n):
    # 1. Generate Data
    M1, M2, M1_odd = compute_tables(limit_n)
    
    print(f"\nScanning integers 2..{limit_n} for Mersenne Primes...")
    print("Criterion: n is Prime AND n+1 is Power of 2")
    print("Formula:   (L_prime(n))^2 + (L_pow2(n+1))^2 == 0\n")
    
    count = 0
    
    # We only verify n where n+1 is a power of 2 (Mersenne Numbers)
    # to show it distinguishes Primes from Composites within that set.
    # But the code runs on ALL n to prove robustness.
    
    for n in range(2, limit_n):
        
        # 1. Check Primality of n
        val_prime = L_prime(n, M1, M2)
        
        # 2. Check Power-of-2 of n+1
        val_pow2  = L_pow2(n+1, M1, M1_odd)
        
        # 3. Fused Invariant
        invariant = (val_prime)**2 + (val_pow2)**2
        
        if invariant == 0:
            count += 1
            print(f"FOUND MERSENNE PRIME #{count}: n = {n}")

if __name__ == "__main__":
    # Search up to 600,000 to catch M19 (524287)
    find_mersenne_primes(600000)
