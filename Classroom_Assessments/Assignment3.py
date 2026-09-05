class Order:
    def __init__(self, oid, nm, bamt):
        self.oid = oid
        self.nm = nm 

        if bamt > 0:
            self.__bamt = bamt
        else:
            print("Amount must be positive!")
            self.__bamt = 0

    def get_base_amount(self):
        return self.__bamt

    def calculate_total(self):
        return self.__bamt

    def display_details(self):
        print("ID:", self.oid)
        print("Name:", self.nm)
        print("Total:", self.calculate_total())


# Derived class[cite: 1]
class PremiumOrder(Order):
    def __init__(self, oid, nm, bamt, dp, fsf):
        super().__init__(oid, nm, bamt)
        self.dp = dp 
        self.fsf = fsf

    def calculate_total(self):
        b = self.get_base_amount()
        disc = b * (self.dp / 100)
        return b - disc + self.fsf

    def display_details(self):
        print("ID:", self.oid)
        print("Name:", self.nm)
        print("Discount:", self.dp, "%")
        print("Shipping:", self.fsf)
        print("Final Bill:", self.calculate_total())

o1 = Order("111", "Anupam", 1000)
o1.display_details()

print()
po1 = PremiumOrder("222", "Abhay", 2000, 15.0, 50.0)
po1.display_details()


class Employee:
    def __init__(self, eid, nm, dpt):
        self.eid = eid 
        self.nm = nm 
        self.dpt = dpt 

    def calculate_salary(self):
        raise NotImplementedError("Not done yet") 

    def display_info(self):
        print("ID:", self.eid, "Name:", self.nm, "Dept:", self.dpt)


class SalariedEmployee(Employee):
    def __init__(self, eid, nm, dpt, ms, td):
        super().__init__(eid, nm, dpt)
        self.ms = ms 
        self.td = td 

    def calculate_salary(self):
        return self.ms - self.td

    def display_info(self):
        super().display_info()
        print("Net Salary:", self.calculate_salary())


# Commission Employee class[cite: 1]
class CommissionEmployee(SalariedEmployee):
    def __init__(self, eid, nm, dpt, ms, td, sa, cr):
        super().__init__(eid, nm, dpt, ms, td)
        self.sa = sa 
        self.cr = cr 

    def calculate_salary(self):
        base_net = super().calculate_salary() 
        comm = self.sa * self.cr
        return base_net + comm 

    def display_info(self):
        print("ID:", self.eid, "Name:", self.nm, "Dept:", self.dpt)
        print("Sales:", self.sa)
        print("Comm Earned:", self.sa * self.cr)
        print("Total Payout:", self.calculate_salary()) 


print()
emp_list = [
    SalariedEmployee(1, "Anupam", "IT", 5000, 500),
    CommissionEmployee(2, "Sarthak", "Sales", 4000, 400, 10000, 0.05)
]

for e in emp_list:
    e.display_info()
    print()