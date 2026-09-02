class Student:
    def __init__(self, name, RegistrationNumber):
        self.name = name
        self.RegistrationNumber = RegistrationNumber
        self.course = None

    def identity(self):
        return f"Student Name: {self.name}, Registration Number: {self.RegistrationNumber} , Student Course: {self.course}"

class undergraduateStudent(Student):
    def __init__(self, name, RegistrationNumber):
        super().__init__(name, RegistrationNumber)
        self.course = "Undergraduate"
    def identity(self):
        return f"Student Name: {self.name}, Registration Number: {self.RegistrationNumber} , Student Course: {self.course}"

class postgraduateStudent(Student):
    def __init__(self, name, RegistrationNumber):
        super().__init__(name, RegistrationNumber)
        self.course = "Postgraduate"
    def identity(self):
        return f"Student Name: {self.name}, Registration Number: {self.RegistrationNumber} , Student Course: {self.course}"

class PhDStudent(Student):
    def __init__(self, name, RegistrationNumber):
        super().__init__(name, RegistrationNumber)
        self.course = "PhD"
    def identity(self):
        return f"Student Name: {self.name}, Registration Number: {self.RegistrationNumber} , Student Course: {self.course}"

Undergraduate = undergraduateStudent("John Doe", "UG12345")
postgraduate = postgraduateStudent("Jane Smith", "PG67890")
PhD = PhDStudent("Alice Johnson", "PHD54321")

print(Undergraduate.identity())
print(postgraduate.identity())
print(PhD.identity())
