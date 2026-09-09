from abc import ABC, abstractmethod
class VendorItem(ABC):
    def __init__(self,item_name,price):
        self.item_name=item_name
        self.price=price

    @abstractmethod
    def calculate_tax(self):
        pass

class DigitalProduct(VendorItem):
    def __init__(self, item_name, price,file_size_mb):
        super().__init__(item_name, price)
        self.file_size_mb=file_size_mb

    def calculate_tax(self):
        return self.price*0.18

    def __add__(self, other):
        return DigitalProduct("{self} & {other}" , self.price+other.price , self.file_size_mb+other.file_size_mb)

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return f"Item name: {self.item_name}, Price: {self.price}, File size(MB): {self.file_size_mb}"


VendorEbook=DigitalProduct("Vendor E-book" , 12.75 , 203.0)
Vendor_Software_License=DigitalProduct("Vendor Software License" , 25.41 , 413.0)

print(VendorEbook.calculate_tax())
print(VendorEbook+Vendor_Software_License)
print(VendorEbook>Vendor_Software_License)
