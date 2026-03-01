"""
Eldon Wu
lab 9, unit testing
feb 28, 2026
"""
class Employee:
    # property
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary 

    @property 
    def emailemployee(self):
        return f"{self.first}_{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"  # fixed: "f{...}" → f"{...}" (missing f-string prefix)
    
    # method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)