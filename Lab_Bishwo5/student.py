class Student:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_student_name(self):
        print(self.name)

    def __repr__(self):
        return "Welcome " + self.name

student1 = Student("Ram", 20, "Kathmandu")
print(student1.location)
student1.location = "Lalitpur"
print(student1.location)
student2 = Student("Shyam", 22, "Kathmandu")
print(student2.location)
