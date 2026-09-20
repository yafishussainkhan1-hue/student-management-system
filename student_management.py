class Student:
    def __init__(self):
        self.name = input("ENTER THE NAME: ")
        self.roll_no = int(input("ENTER THE ROLL NUMBER: "))
        self.python = float(input("ENTER THE PYTHON MARKS: "))
        self.maths = float(input("ENTER THE MATHS MARKS: "))
        self.data_science = float(input("ENTER THE DATA SCIENCE MARKS: "))
    def percentage(self):
        total = self.python + self.maths + self.data_science
        percentage = total / 3
        return percentage
    def result(self):
        if self.percentage() >=40:
            return "Pass"
        else:
            return "Fail"
    def grade(self):
        if self.percentage() >= 90:
            return "A"
        elif self.percentage() >= 80:
            return "B"
        elif self.percentage() >= 70:
            return "C"
        elif self.percentage() >= 60:
            return "D"
        elif self.percentage() >=50:
            return "E"
        else:
            return "F"
students = []
while True:
    s = Student()
    students.append(s)
    choice = input("Do you want to add more Students (yes/no): ")
    if choice.lower() == "no":
        break  
print("\n -----Students Result----- ") 
for student in students:  
  print("Name: ", student.name)    
  print("Roll Number: ", student.roll_no)
  print("Percentage: ", student.percentage())
  print("Result: ", student.result())
  print("Grade", student.grade())
  print("-------------------------")
