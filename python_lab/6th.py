'''
Develop a program to sort the contents of a text file and write the sorted contents into
a separate text file.
'''

# Open the input file for reading
input_file = '/home/himanshu/Desktop/python_lab/input.txt'
with open(input_file, 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

# Sort the contents
sorted_contents = sorted(contents)

# Open the output file for writing
output_file = '/home/himanshu/Desktop/python_lab/output.txt'
with open(output_file, 'w') as file:
    # Write the sorted contents to the output file
    file.writelines(sorted_contents)

print("File sorted and written to", output_file)