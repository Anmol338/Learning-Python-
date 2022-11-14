class Student:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_student_name(self):
        return self.name

    def set_student_name(self, new_name):
        self.name = new_name

    def __repr__(self):
        return "Welcome " + self.name

student1 = Student("Ram", 20, "Kathmandu")
print(student1.get_student_name())

student1.set_student_name("Reena")
print(student1.get_student_name())