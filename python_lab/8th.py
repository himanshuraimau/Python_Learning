'''
Write a function named DivExp which takes TWO parameters a, b and returns a value
c (c=a/b). Write suitable assertion for a>0 in function DivExp and raise an exception
for when b=0. Develop a suitable program which reads two values from the console
and calls a function DivExp.'''

def DivExp(a, b):
    assert a > 0, "a must be greater than 0"
    if b == 0:
        raise Exception("b cannot be zero")
    return a / b

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

try:
    result = DivExp(a, b)
    print("Result:", result)
except AssertionError as e:
    print("Assertion Error:", e)
except Exception as e:
    print("Exception:", e)
