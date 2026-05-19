"""
    this is day 2 of my python learning 
    and today i am going to 
    Goal: learn how to read/write local files and use python to 
          commiunicate directly with the plateform servers 
   
    in C++ we handle files like freopen or #include <fstream> with ofstream
    while in python we use ## with open() which automatically handle closing 
    the file so we don't have to worry about memory leaks.
    
    File Modes:
    "r" - read (default)
    "w" - write (truncates the file if it already exists)
    "a" - append (writes to the end of the file if it already exists)
    "x" - create (creates a new file, but fails if the file already exists
    "rb" - read binary
    
    ## writing to a file:
    file.write is use to write content to a file 
    ** what is with ???
    
       with: means Open file temporarily ans automatically close if afterward.
    
    ** what is as file ???
       as file: atores teh opened file object in variable file.
       
    ## Reading to a file:
    
    file.read() is used to read the content fo a file
    content = file.read() # reads the entire file content 
"""
 
# Writing to a file 
with open("error.txt", "w") as file:
    file.write("This is an error file created by arpit jatav")
    
#Reading from that file
with open("error.txt", "r") as file:
    content = file.read()
    print(content)
    

# Appending content to a file 
with open("error.txt", "a") as file:
    file.write("\nThis is an appended line")

# reading from file once again to see the changes 
with open("error.txt", "r") as file:
    text=file.read()
    print(text)
    
    
# writing a practice file 
name = input("Enter your name: ")
age = int(input("Enter your age: "))

with open("Data.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n") 

with open("Data.txt", "r") as file:
    data =file.read()
    print(data)

