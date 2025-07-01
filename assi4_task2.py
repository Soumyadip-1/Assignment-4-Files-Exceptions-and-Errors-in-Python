# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


t_write = input("Enter text to write to the file : ")
with open("output.txt","w") as file:
    file.write(t_write+'\n')
print("Data successfully writen to output.txt")

t_append = input("Enter text to append to the file : ")
with open('output.txt','a') as file:
    file.write(t_append+'\n')
print("Data append successfully to output.txt")

print("\nFinal content of file : \n")
with open("output.txt",'r') as file:
    print(file.read())
