class InvalidDaysError(Exception):
    def __init__(self, message="Days overdue cannot be negative"):
        super().__init__(message)

class LibraryBook:
    def __init__(self,book_id,title,base_fine):
        self.book_id=book_id
        self.title=title
        if not isinstance(base_fine , float):
            raise TypeError("base_fine must be a float")

        if base_fine<=0:
            raise ValueError("base_fine must be positive")
        self.__base_fine=base_fine

    def get_base_fine(self):
        return self.__base_fine

    def calculate_penalty(self,days_overdue):
        if days_overdue<0:
            raise InvalidDaysError(f"Invalid days ({days_overdue}) for book {self.book_id}")
        return days_overdue*self.__base_fine

    def display_details(self,days_overdue):
        print("book id:" ,self.book_id)
        print("Book Title:" , self.title)
        print(f"Base Penalty: {days_overdue * self.get_base_fine()}")

class ReferenceBook(LibraryBook):
    def __init__(self, book_id, title, base_fine,fixed_processing_fee):
        super().__init__(book_id, title, base_fine)

        if not isinstance(fixed_processing_fee,float):
            raise TypeError("fixed_processing_fee must be a float")

        self.fixed_processing_fee=fixed_processing_fee

    def calculate_penalty(self, days_overdue):
        return super().calculate_penalty(days_overdue) + self.fixed_processing_fee

    def display_details(self, days_overdue):
        super().display_details(days_overdue)
        print("Fixed Processing Fee:", self.fixed_processing_fee)
        print("Total Penalty:", self.calculate_penalty(days_overdue))


LB=LibraryBook("001","First Book",12.5)
RB=ReferenceBook("002","First Reference Book",10.5,2.35)

List1={LB,RB}

for i in List1:
    i.display_details(5)

try:
    LB.display_details(-5)
except InvalidDaysError as e:
    print("Caught an error:", e)
finally:
    print("Program Executed successfully.")