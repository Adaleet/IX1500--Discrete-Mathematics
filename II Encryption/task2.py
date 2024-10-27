import sympy
import time
import pandas as pd
import matplotlib.pyplot as plt

e = 65537  # A common public exponent

# Function to generate an RSA modulus n with the desired number of bits
def generate_rsa_modulus(bits): 
    # Since we'll only be measuring for an x desired amount of bits instead of the long cipher block
    p = sympy.randprime(2**(bits // 2 - 1), 2**(bits // 2))
    q = sympy.randprime(2**(bits // 2 - 1), 2**(bits // 2))
    return p * q, p, q

# Function to measure the time to crack the desired RSA message
def cracking_time(bits, message): 
    # Generate RSA modulus n of specified bit size
    n, p, q = generate_rsa_modulus(bits) 
    phi_n = (p - 1) * (q - 1)
    
    # Finding the private key 'd' (not used for decryption timing here)
    d = sympy.mod_inverse(e, phi_n)
    
    # Encrypt the specific message
    cipher = pow(message, e, n)
    
    # Start timing the factorization step
    start_fact_time = time.time()
    factors = sympy.factorint(n)
    end_fact_time = time.time()
    fact_time = end_fact_time - start_fact_time

    # Validating that n is a product of two primes
    primes = list(factors.keys())
    if len(primes) != 2:
        raise ValueError("n is not a product of two primes.")
    
    return fact_time

# Encode the specific message as an integer for RSA encryption
message = int.from_bytes(b"GO DOWN DEEP ENOUGH INTO ANYTHING AND YOU WILL FIND MATHEMATICS.", "big")

# Test across different bit sizes and collect results
results = []
for bits in range(100, 201, 10):
    fact_time = cracking_time(bits, message)
    results.append({
        "Bit Size": bits,
        "Factorization Time (s)": fact_time,
    })
    print(f"Bit Size: {bits} | Factorization Time: {fact_time} s")

# Output results in a table or visualize if necessary
df = pd.DataFrame(results)
print(df)

# Plotting results
plt.figure(figsize=(10, 5))
plt.plot(df["Bit Size"], df["Factorization Time (s)"], label="Factorization Time")
plt.xlabel("RSA Key Size (bits)")
plt.ylabel("Time (seconds)")
plt.title("RSA Cracking Time by Key Size")
plt.legend()
plt.show()
