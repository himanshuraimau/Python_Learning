'''Read N numbers from the console and create a list. Develop a program to print
mean, variance andstandard deviation with suitable messages.'''

import numpy as np
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)
mean = np.mean(numbers)
variance = np.var(numbers)
std_deviation = np.std(numbers)
print(f"Mean: {mean}")
print(f"Variance: {variance}")

print(f"Standard Deviation: {std_deviation}")

