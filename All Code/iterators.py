# x=[10,20,30,40]
# it=iter(x)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))             #It gives stopIeration no more items..


it=iter([10,20,30,40])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break