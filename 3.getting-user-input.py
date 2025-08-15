#prompting for input from a users

name = input("Enter Your Name: ")
remarks = f"Welcome {name}, to the python community"

print(remarks)

""" 
What is happening here?
- Using the built in input function to prompt for input. The it is later stored in a variable called name.
- Since we stored the value of the input in the name variable, using the f-string to create a message of a string
- The print function helps us to access the value at the time of execution.
 """