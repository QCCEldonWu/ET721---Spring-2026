"""
Eldon Wu
March 3, 2026
lab 10, unit testing using pytest
"""
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b
"""
# testing
print(add(2,3)) # 5
print(add(-8,5)) # -3
print(subtract(7, 5)) # 2
print(subtract(-7, 5)) #-12
print(subtract(-7, -5)) # -2
"""
# lab exercise 1: basic testing
def divide(a,b):
    if (b == 0):
        raise ValueError("Cannot divide by zero")
    return a / b

# local testing
# print(divide(5,2)) # 2.5
# print(divide(3,0)) # should raise an error

# lab exercise 2: password validation: 8+ characters, and can't have # % and whitespace in between
def validate_password(password):
    password.strip() # removing leading and ending whitespace
    special_character = '%' in password or '#' in password or ' ' in password
    if len(password) < 8 or special_character:
        return False
    return True
"""
# local testing
print(validate_password("peterpan"))  #true
print(validate_password("peter pan")) #false
print(validate_password("peter#pan")) #false
print(validate_password("peter%pan")) #false
print(validate_password("peter$pan")) #true
print(validate_password("pan"))       #false
"""

# lab exercise 3: test if a number is even
def is_even(n):
    return (n % 2 == 0 and n != 0) 
"""
# local testing
print(is_even(8))   #true
print(is_even(-5))  #false
print(is_even(0))   #false
print(is_even(-12))  #true
print(is_even(11))  #false
"""