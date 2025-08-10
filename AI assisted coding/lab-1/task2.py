def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# Main program
terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci_sequence(terms)
print(f"Fibonacci sequence: {fib_seq}")