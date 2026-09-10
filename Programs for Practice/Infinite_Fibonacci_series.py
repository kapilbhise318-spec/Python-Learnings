# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# f1=fibonacci()

# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))




def fibonacc_series():
    a,b=0,1

    while True:
        yield a
        a,b=b, a+b
f2=fibonacc_series()
print(next(f2))
print(next(f2)) 
print(next(f2)) 
print(next(f2)) 
print(next(f2)) 
print(next(f2)) 