def numbers():
    yield 10
    yield 20
    yield 30
gen=numbers()
print(next(gen))
print(next(gen))
print(next(gen))