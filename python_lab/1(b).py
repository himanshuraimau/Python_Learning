'''Develop a program to read the name and year of birth of a person. Display
whether the person is a senior citizen or not.'''


name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2021
age = current_year - year_of_birth
if age >= 60:
    print(name, "is a senior citizen.")
else:
    print(name, "is not a senior citizen.")
    