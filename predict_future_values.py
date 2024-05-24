import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import islice


def estimate_lcg_parameters(sequence):
    n = len(sequence)
    diffs = np.diff(sequence)
    
    # Estimating 'm' (modulus)
    m_est = np.gcd.reduce(diffs)
    
    # Estimating 'a' and 'c'
    a_est = []
    c_est = []
    for i in range(1, n - 1):
        a = (sequence[i + 1] - sequence[i]) * pow((sequence[i] - sequence[i - 1]), -1, m_est) % m_est
        c = (sequence[i + 1] - a * sequence[i]) % m_est
        a_est.append(a)
        c_est.append(c)
    
    a_est = int(np.median(a_est))
    c_est = int(np.median(c_est))
    
    return a_est, c_est, m_est


def main():
    # Read data from the text file
    file_path = 'data/raw/numbers.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            data = np.array([float(value.replace('x', '')) for value in content.split(',')])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except ValueError:
        print("Error reading the data from the file. Ensure the file contains only numeric values.")
        return
    
    if len(data) < 3:
        print("Not enough data to estimate LCG parameters.")
        return
    
    # Estimate LCG parameters
    a, c, m = estimate_lcg_parameters(data)
    print(f"Estimated LCG parameters: a = {a}, c = {c}, m = {m}")
    
    # Initialize the LCG with estimated parameters
    X = [data[0]]
    for _ in range(len(data) - 1):
        X.append((a * X[-1] + c) % m)
    
    # Theoretical Weakness Analysis
    observed = data[:len(X)]
    predicted = np.array(X)
    
    # Period Analysis
    period = len(set(predicted))
    print(f"Estimated period of the sequence: {period}")
    
    # Distribution Analysis
    plt.figure(figsize=(10, 6))
    plt.hist(observed, bins=20, alpha=0.5, label='Observed')
    plt.hist(predicted, bins=20, alpha=0.5, label='Predicted')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of Observed and Predicted Values')
    plt.legend()
    plt.show()
    
    # Correlation Analysis
    plt.figure(figsize=(10, 6))
    plt.scatter(observed, predicted, alpha=0.5)
    plt.xlabel('Observed Values')
    plt.ylabel('Predicted Values')
    plt.title('Correlation between Observed and Predicted Values')
    plt.show()


if __name__ == "__main__":
    main()
    if len(sequence) < 3:
        print("Not enough data to estimate LCG parameters.")
        return
    
    # Estimate LCG parameters
    a, c, m = estimate_lcg_parameters(sequence)
    print(f"Estimated LCG parameters: a = {a}, c = {c}, m = {m}")
    
    # Initialize the LCG with estimated parameters
    X = [sequence[0]]
    for _ in range(len(sequence) - 1):
        X.append((a * X[-1] + c) % m)
    
    # Theoretical Weakness Analysis
    observed = sequence[:len(X)]
    predicted = np.array(X)
    
    # Period Analysis
    period = len(set(predicted))
    print(f"Estimated period of the sequence: {period}")
    
    # Distribution Analysis
    plt.figure(figsize=(10, 6))
    plt.hist(observed, bins=20, alpha=0.5, label='Observed')
    plt.hist(predicted, bins=20, alpha=0.5, label='Predicted')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of Observed and Predicted Values')
    plt.legend()
    plt.show()
    
    # Correlation Analysis
    plt.figure(figsize=(10, 6))
    plt.scatter(observed, predicted, alpha=0.5)
    plt.xlabel('Observed Values')
    plt.ylabel('Predicted Values')
    plt.title('Correlation between Observed and Predicted Values')
    plt.show()


if __name__ == "__main__":
    main()
    plt.legend()
    plt.show()

    # Display predictions
    print("Predicted values for the next 5 indices:", predictions)

if __name__ == "__main__":
    main()
