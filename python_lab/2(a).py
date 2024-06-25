'''Develop a program to generate Fibonacci sequence of length (N). Read N from
console.'''

# Read the length of the Fibonacci sequence from the console
n = int(input("Enter the length of the Fibonacci sequence: "))
# Initialize the first two Fibonacci numbers
fibonacci_sequence = [0, 1]
# Generate the Fibonacci sequence
for i in range(2, n):
    next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(next_number)
# Print the Fibonacci sequence
print("Fibonacci Sequence:")
print(fibonacci_sequence)
