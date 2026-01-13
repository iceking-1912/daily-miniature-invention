"""
Fibonacci Sequence Generator
----------------------------
This program generates the Fibonacci sequence up to a specified number of terms.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
"""

def generate_fibonacci(n_terms):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == "__main__":
    terms = 10
    print(f"Generating first {terms} terms of the Fibonacci sequence:")
    print(generate_fibonacci(terms))
