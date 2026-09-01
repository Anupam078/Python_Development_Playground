class Employee:
    da=.60
    def __init__(self,grade,basic_salary):
        self.grade = grade
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.gross_salary = self.basic_salary + (self.basic_salary * Employee.da)


    def display_info(self):
        print(f"Grade and Basic Salary is {self.grade} and {self.basic_salary}")
        print(f"Gross Salary is {self.gross_salary}")
        print(f"DA is {Employee.da}") 

    @classmethod
    def da_class(cls):
        return (f"All employees get DA {cls.da}")

    @staticmethod
    def is_more_than(basic_salary, avg_salary):
        return basic_salary > avg_salary
    
