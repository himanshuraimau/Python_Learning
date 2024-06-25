'''Read a multi-digit number (as chars) from the console. Develop a program to print
the frequency ofeach digit with suitable message.'''


# Read a multi-digit number from the console
number = input("Enter a multi-digit number: ")

# Initialize a dictionary to store the frequency of each digit
digit_frequency = {}

# Iterate through each character in the number
for digit in number:
    # Check if the character is a digit
    if digit.isdigit():
        # Increment the frequency of the digit in the dictionary
        digit_frequency[digit] = digit_frequency.get(digit, 0) + 1

# Print the frequency of each digit
for digit, frequency in digit_frequency.items():
    print(f"The digit {digit} appears {frequency} times.")