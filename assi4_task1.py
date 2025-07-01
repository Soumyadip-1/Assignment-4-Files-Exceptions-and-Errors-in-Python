# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


try:
    with open("sample.txt","r") as file:
        print("\nReading the file content : ")
        for line in file:
            print(line.strip())
    print("\nEX- error handeling")
    with open("samp.txt","r") as file1:
        content = file1.read()
        print(content)
except FileNotFoundError:
    print("ERROR !! file not found \n continue....")
    