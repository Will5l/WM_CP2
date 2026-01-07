def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator
def greet():
    print("Hello, World")

greet()

@decorator
def add():
    print(1+1)

add()