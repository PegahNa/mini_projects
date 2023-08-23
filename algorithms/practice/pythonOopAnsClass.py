# Design a parent class called CFGStudent. It should have general attributes like name, surname, age, email, student id and methods to fetch student’s full name and student’s id. 
# Important: there should be an option to pass student id when a new class object is generated, HOWEVER, if no id is passed, then student_id should be automatically generated and assigned to the class.
# Design a child class called NanoStudent, which inherits from CFGStudent class. This class should have exactly the same attributes as its parent class, as well as additional two called ‘specialization’ and ‘course grades’. 
# The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’ in front of the id. 
# New methods ‘add_new_grade’ and ‘get_course_grades’ should be added. Please see the skeleton structure in the final_assessment.py file. You can use it as a skeleton code for your classes OR adjust it and create your own. 
# SEE ADDITIONAL COMMENTS in the file. 
import random
import string

class CFGStudent:
    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id if student_id else self.generate_student_id()

    def generate_student_id(self):
        return "CFG" + ''.join(random.choices(string.digits, k=5))

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_student_id(self):
        return self.student_id

class NanoStudent(CFGStudent):
    def __init__(self, name, surname, age, email, student_id=None, specialization=None):
        super().__init__(name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = {}

    def generate_student_id(self):
        return "NANO" + super().generate_student_id()

    def add_new_grade(self, course, grade):
        self.course_grades[course] = grade

    def get_course_grades(self):
        return self.course_grades

# Example usage
nano_student = NanoStudent("Alice", "Johnson", 25, "alice@example.com", specialization="Machine Learning")
nano_student.add_new_grade("Math", 85)
nano_student.add_new_grade("Computer Science", 90)
nano_student.add_new_grade("Data Science", 78)

print("Nano Student - Full Name:", nano_student.get_full_name())
print("Nano Student - Student ID:", nano_student.get_student_id())
print("Nano Student - Specialization:", nano_student.specialization)
print("Nano Student - Generated ID:", nano_student.generate_student_id())
print("Nano Student - Course Grades:", nano_student.get_course_grades())