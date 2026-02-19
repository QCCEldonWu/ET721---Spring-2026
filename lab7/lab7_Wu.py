"""
Eldon Wu
Feb 19, 2026
lab 7 working with data
"""
print("\n ----- Eaxample 1: read file -----")
with open("lab7/phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

#check if the file is closed
print(f"Is the file closed? {file1.closed}")

print("\n ----- Eaxample 2: readline file -----")
with open("lab7/phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)

print("\n ----- Eaxample 3: readlines file -----")
# readlines make a list of all the lines in the text file. Each line is an item in the list
with open("lab7/phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)

print("\n ----- Eaxample 3: loop through each line in a file -----")
with open("lab7/phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) # strip() method removes \n in each line

print("\n ----- Example 5: create file -----")
#w mode create a file if the file doesn't exist. On the other hand, if the file exists, w mode will overwrite the data in the file
with open("lab7/wu.txt", "w") as file:
    file.write("Python basics for data science\n")
    file.write("Eldon Wu")

print("\n ----- Example 6: append data into an existing file -----")
# append the date and time into "lastname.txt" file
from datetime import datetime

with open("lab7/wu.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")

print("\n ----- Example 7: copy a file -----")
#copy file "lastname.txt" into a new file
with open("lab7/wu.txt", "r") as readfile:
    with open("lab7/newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)
"""
print("\n ----- Example 8: pandas a file -----")
import pandas as pd

data ={
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

print("\n ----- Example 9: creating df with pandas from an excel file -----")
df = pd.read_excel("lab7/classdata.xlsx")
print(df)
print(df.head())
"""
print("\n ----- EXERCISE -----")
def email_read():
    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0
    try:
        with open("lab7/user_email.txt", "r") as file:
            for line in file:
                if "@gmail" in line:
                    gmail_count += 1
                elif "@yahoo" in line:
                    yahoo_count += 1
                elif "@hotmail" in line:
                    hotmail_count += 1
        with open("lab7/reportemail.txt", "w") as reportfile:
            reportfile.write(f"gmail = {gmail_count}\n")
            reportfile.write(f"yahoo = {yahoo_count}\n")
            reportfile.write(f"hotmail = {hotmail_count}\n")
    except FileNotFoundError:
        print("The file user_email.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

email_read()
