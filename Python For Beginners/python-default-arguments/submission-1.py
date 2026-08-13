# since first parameter has a default value, all other parameters must also have one
def greet(name="World", punctuation="!") -> None:
    print("Hello, " + name + punctuation)

greet("World", "!")
greet("World")
