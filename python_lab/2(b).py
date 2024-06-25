'''Write a function to calculate factorial of a number. Develop a program to
compute binomialcoefficient (Given N and R).'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binomial_coefficient(n, r):
    if r > n:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n-r))

# Example usage
n = 5
r = 2
result = binomial_coefficient(n, r)
print(f"The binomial coefficient of {n} and {r} is {result}")