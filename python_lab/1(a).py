'''Develop a program to read the student details like Name, USN, and Marks in
three subjects. Display the student details, total marks and percentage with
suitable messages'''


name = input("Enter student name: ")
usn = input("Enter student USN: ")
marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

print("Student Details:")
print("Name:", name)
print("USN:", usn)
print("Marks in Subject 1:", marks1)
print("Marks in Subject 2:", marks2)
print("Marks in Subject 3:", marks3)
print("Total Marks:", total_marks)
print("Percentage:", percentage)