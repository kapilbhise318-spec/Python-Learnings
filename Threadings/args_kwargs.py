# def add(*args):
#     print(args)
#     return (sum(args))
# print(add(5, 121, 45))
# print(add(10, 25, 30))
# add(14, 52)



# You can mix *args with regular parameters..

# def greetings(greetings, *names):
#     for name in names:
#         print(f"{greetings}, {name}.")
# greetings("Congratulations", "Alice_borderland", "Bob_Marley", "Carlos_Alcaraz")




# def show_info(**kwargs):
#     print(kwargs)


# show_info(name="Alice", age=30, city="NYC", Location="8085 localHost")




# iteratng over **kwargs

def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}")

display(language="German", value=8.89)