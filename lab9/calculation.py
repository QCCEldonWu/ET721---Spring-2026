"""
Eldon Wu
lab 9, unit testing
feb 28, 2026
"""
def addthreenumbers(n1=0, n2=0, n3=0):
    return n1+n2+n3

def subtracttwonumbers(n1=0, n2=0):   
    return n1-n2

def multiplythreenumbers(n1, n2, n3):
    return n1*n2*n3

def dividetwonumbers(n1, n2):
    try: 
        return n1/n2
    except ZeroDivisionError:
        print("ERROR! cant divide by zero")
    except ValueError:
        print("ERROR! not a numerical value")
    except:
        print("ERROR! cant divide the numbers")