def decorator(func):
    def wrapper():
        print("Transaction initiated.")
        func()
        print("Transaction Completed.")

    return wrapper
@decorator
def hello():
    print("Executing all steps transaction..")
hello()
