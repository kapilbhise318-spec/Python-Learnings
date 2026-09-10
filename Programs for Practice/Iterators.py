elements=['apple','banana','mango','kivi']

it=iter(elements)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # it gives StopIteration error
print('---***---')
print()


# print infinite numbers

def infinite_numbers():
    n=1
    while True:
        yield n
        n  = n + 1
iterss=infinite_numbers()
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
print(next(iterss))
