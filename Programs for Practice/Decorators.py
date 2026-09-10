def my_decorator(func):
    def wrapper():
        print("Before function runs...")

        func()

        print("After function runs...")
    return wrapper

@my_decorator
def hello():
    print("***Hello_Python***")
hello()
print()




def decorators(func):
    def wrapper():
        print('Before function calls...')
        func()
        print('After function calling...')
    return wrapper

@decorators
def greet():
    print('---Hello---')
greet()
print()





# Decorators with parameters...

from functools import wraps

def repeat(n):

    def decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):
            for _ in range (n):
                func(*args, **kwargs)

        return wrapper
    
    return decorator

@repeat(5)
def greet():
    print('Hello World!')
greet()