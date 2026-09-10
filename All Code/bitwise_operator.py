# a =10
# b=20
# print(a & b)


# def greeting():
#     print("welcome to python Tutorial")
# greeting()





# def grrting(name,city):
#     print(f"Nice to meet you, {name} and i heard lots of about your{city}")
# grrting("Sam","NYC")
# 
# 


# def s(name="Shah Rukh Khan"):
#     print("The name is, " + name + "!")
# s()
# # s("Madanan")



# def d(a,b):
#     return a/b
# r=d(b=10, a=5)
# print(r)


# rr=d(2000,100)
# print(rr)




# def add_nummbers(*args):
#     return sum(args)

# numbers=add_nummbers(10,12,14,50,14)
# print(numbers)




# def greetings(*names):
#     # print()
#     for i in names:
#         print(f"Hi and nice to meet you {i} !")
# greetings ("Saumya","Ramya","Ananya")





# def details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# details(name="Kapil",age=27,city="Pune")







def shopping_cart(**Products):
    total=0
    print("Product Purchased: ")
     
    for item, price in Products.items():
        print(f"{item}: ${price}")
        total +=price
    print(f"total,${total}")

shopping_cart(apple=15, Orange=20, Coconut=80)