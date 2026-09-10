# data=[[10,20,[20,30],[50],[30,45]]]
# Result=[]

# for numbers in data:
#     for number in numbers:
#         Result.append(number)
# print(Result)

listen=[1,2,[7,9,[15,[12,9]],18,10]]

def flatten_list(listen):
    l=[]
    for i in listen:
        if (type(i) is list):
            l.extend(flatten_list(i))
        else:
            l.append(i)
    return l
print(flatten_list(listen))