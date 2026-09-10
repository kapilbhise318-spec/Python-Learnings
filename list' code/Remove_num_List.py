# list=[10,20,30,40,50,60,70,60]
# remove_number=int(input("enter a number to from the lise: "))
# new_list=[]

# for i in list:
#     if i != remove_number:
#         new_list.append(i)
# print(new_list)



# 2).. if condition

a=[1,2,3]
b=int(input("enter number to remove: "))

if b in a:
    a.remove(b)
    print(a)

else:
    print("number not found...")