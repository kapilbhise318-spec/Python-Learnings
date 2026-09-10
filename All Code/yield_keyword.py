# def numbers():
#     yield 1
#     yield 2
#     yield 3

# for num in numbers():
#     print(num)


# def numbers():
#     yield 10
#     yield 20
#     yield 30

# gen = numbers()
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))





def c(r):
    i=1
    while i<=r:
        yield i
        i+=1

for num in c(10):
    print(num)
