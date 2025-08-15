l = ["Python", "Java", "Javascript"]
t = ("Python", "Java", "Javascript")
s = {"Python", "Java", "Javascript"}

#you can access the elements of a collection using subscript notation. 
#the first element of a collection has an index of [0] and the rest follow sequencially. [0],[1],[2]
#Accessing the elements is commonly used with lists and tuples, but for sets it does not make sense since it is not orderly.

l[2] = "Go"
print(l)

#You will get an error when trying to alter the elements in a tuple
t[1]
print(t)

#Tuples can not be modified whenever they are created
#sets also do not allow subscript notation

#You can add items to a list by using Append function

l.append("Go")
print(l)

l.remove("Java")
print(l)

#Sets are not orderly, but we can add elements to it; and it wont maintain the order. 
s.add("TypeScript")
print(s)