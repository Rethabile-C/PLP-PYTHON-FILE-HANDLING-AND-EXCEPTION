file = open("assignment_week3.txt", "w")
file.write("Hello everyone")



#Create a program that reads a file 

file = open("assignment_week3.txt", "r")
content = file.read()
print(content)



#writes a modified version to a new file.

file= open("assignment_week3.txt", "a")
file.write("my Shaila")


#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    file = open("assignment_week3.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")

