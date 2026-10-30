'''class BookStore:
    def __init__(self,attribute1,attribute2):
        self.instAtt1=attribute1
        self.instAtt2=attribute2

book1=BookStore("Python Textbook",500)

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def display(self):
        print(self.name)
        print(self.roll_number)

Std1=Student("Rahul",1)
Std2=Student("Rohan",2)
Std1.display()
Std2.display()'''
    
'''class Employee:
    company_name="TechCorp"
    def __init__(self,emp_id):
        self.emp_id=emp_id

    @classmethod
    def get_company(cls):
        return cls.company_name


Emp1=Employee(001);
print(Emp1.emp_id)
print(Employee.company_name)

emp1 = Employee(101)
hasattr(emp1,"salary")
setattr(emp1,"Salary",5000)
print(getattr(emp1,"salary"))
delattr(emp1,"salary")'''


class Printer:
    def __init__(self):
        pass

    def print_document(self, text, copies=1):
        for i in range(0,copies):
            print(text)

p1=Printer()
p1.print_document("Sample Text")
p2=Printer()
p2.print_document("Sample Document",3)

class calculator:
    def __init__(self):
        pass

    def add_numbers(self, *args):
        sum=1
        for num in args:
            sum+=num
        return sum

c1=calculator()
c1.add_numbers(10, 20, 30, 40)
        