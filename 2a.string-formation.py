#Template Strings with .format()

name = "Bob"
greeting = "hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)

#Creating longer templates
longer_phrase = "Hello, {}. We are learning {}."

formatted = longer_phrase.format("Everyone", "Python")

print(formatted)