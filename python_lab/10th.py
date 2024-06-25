class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        self.marks =[]
        Student.count += 1
    def add_marks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: " %(self.name, i+1)))
            self.marks.append(m)
    def calculate_total(self):
        return sum(self.marks)
    def calculate_percentage(self):
        return self.calculate_total()/3
    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)
        print("Total: ", self.calculate_total())
        print("Percentage: ", self.calculate_percentage())
name = input("Enter the name of the student: ")
s1 = Student(name)
s1.add_marks()
s1.display()

name = input("Enter the name of the student: ")
s2 = Student(name)
s2.add_marks()
s2.display()
