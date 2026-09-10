# def greet(name):
#     print(f"Hello {name}.")
# greet(("Alice"))


# default parameter

# def greet(name,greetings="FairEnonuh"):
#     print(f"{greetings}, {name}.")
# greet("Bpb")
# greet("Bob","world")

# Docstring

# def add(a,b):
#     return (a+b)
# help(add)

def add(a, b):
    # """Return the sum of a and b."""
    return a + b

help(add)   # prints the docstring